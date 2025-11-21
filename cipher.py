BLOCK_SIZE = 4  # 4 byte = 32 bit blok

# PASS → KEY DÖNÜŞÜMÜ (KDF)

def passphrase_to_key(passphrase: str):
    """
    Kullanıcının unutmayacağı bir metni (renk, hayvan adı vs.)
    4 byte'lık bir key'e dönüştürür.
    """
    data = passphrase.encode("utf-8")
    s = sum(data)

    key = [
        s % 256,
        (s * 3) % 256,
        (s * 7 + 5) % 256,
        (s * 13 + 11) % 256
    ]
    return key


# Blok İşlemleri

def text_to_blocks(text: str):
    data = text.encode("utf-8")
    padding_len = (-len(data)) % BLOCK_SIZE

    if padding_len > 0:
        data += b"\x00" * padding_len

    blocks = []
    for i in range(0, len(data), BLOCK_SIZE):
        blocks.append(list(data[i:i+BLOCK_SIZE]))

    return blocks


def blocks_to_text(blocks):
    flat = []
    for b in blocks:
        flat.extend(b)

    data = bytes(flat).rstrip(b"\x00")
    return data.decode("utf-8", errors="ignore")


# Round İşlemleri

def sub_bytes(block):
    return [(b * 7 + 3) % 256 for b in block]


def inv_sub_bytes(block):
    return [((b - 3) * 183) % 256 for b in block]


def xor_with_key(block, key):
    return [block[i] ^ key[i] for i in range(BLOCK_SIZE)]


def rotate_left(block, n=1):
    n = n % BLOCK_SIZE
    return block[n:] + block[:n]


def rotate_right(block, n=1):
    n = n % BLOCK_SIZE
    return block[-n:] + block[:-n]


# Encrypt / Decrypt

def encrypt_block(block, key):
    state = block[:]
    for _ in range(3):
        state = sub_bytes(state)
        state = xor_with_key(state, key)
        state = rotate_left(state)
    return state


def decrypt_block(block, key):
    state = block[:]
    for _ in range(3):
        state = rotate_right(state)
        state = xor_with_key(state, key)
        state = inv_sub_bytes(state)
    return state


def encrypt_text(text, key):
    blocks = text_to_blocks(text)
    encrypted = [encrypt_block(b, key) for b in blocks]
    return encrypted


def decrypt_text(hex_string, key):
    """
    Kullanıcıdan gelen HEX formatındaki şifreli veriyi çözer.
    """
    parts = hex_string.split("|")
    blocks = []

    for part in parts:
        part = part.strip()
        if not part:
            continue
        hex_bytes = part.split()
        block = [int(h, 16) for h in hex_bytes]
        blocks.append(block)

    decrypted = [decrypt_block(b, key) for b in blocks]
    return blocks_to_text(decrypted)


# Yardımcı HEX formatı

def format_blocks_as_hex(blocks):
    return " | ".join(" ".join(f"{b:02x}" for b in block) for block in blocks)


# Kullanıcı Arayüzü (Menu)

def menu():
    print("\n=== MiniBlockCipher ===")
    print("1) Metin Şifrele")
    print("2) Şifre Çöz")
    print("3) Çıkış")
    return input("Seçimin: ")


# Ana Program

if __name__ == "__main__":
    while True:
        sec = menu()

        if sec == "1":
            metin = input("\nŞifrelemek istediğin metni gir: ")
            passphrase = input("Anahtar (unutmayacağın bir kelime): ")
            key = passphrase_to_key(passphrase)

            enc_blocks = encrypt_text(metin, key)

            print("\n[+] Şifreli (HEX):")
            print(format_blocks_as_hex(enc_blocks))

        elif sec == "2":
            sifreli = input("\nÇözmek istediğin HEX metin:\n> ")
            passphrase = input("Aynı anahtarı (kelimeyi) gir: ")
            key = passphrase_to_key(passphrase)

            try:
                sonuc = decrypt_text(sifreli, key)
                print("\n[+] Çözülen Metin:", sonuc)
            except:
                print("[-] Hatalı format veya yanlış passphrase!")

        elif sec == "3":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim!")

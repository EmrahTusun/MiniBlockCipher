<h1>MiniBlockCipher</h1>

<p>
MiniBlockCipher, kullanıcıdan aldığı bir metni ve anahtar kelimeyi kullanarak metni şifreleyen küçük bir Python uygulamasıdır.
Program metni 4 byte'lık bloklara ayırır ve her blok üzerinde belirli dönüşümler uygulayarak HEX formatında bir şifreli çıktı üretir.
Aynı şifreli veri ve doğru anahtar kelime kullanılarak metin tekrar çözülebilir.
Anahtar kelime farklı girilirse çözüm işlemi başarısız olur.
</p>

<h2>Özellikler</h2>
<ul>
  <li>Metin şifreleme</li>
  <li>Şifre çözme</li>
  <li>Kullanıcıdan alınan kelimeyi otomatik olarak anahtar haline dönüştürme</li>
  <li>HEX formatında şifreli çıktı üretme</li>
  <li>Basit komut satırı arayüzü</li>
</ul>

<h2>Kullanım</h2>

<h3>Şifreleme</h3>
<ol>
  <li>Uygulamayı çalıştırın:
    <pre>python cipher.py</pre>
  </li>
  <li>Menüden "1) Metin Şifrele" seçeneğini seçin.</li>
  <li>Şifrelenecek metni girin.</li>
  <li>Anahtar olarak kullanılacak kelimeyi girin.</li>
  <li>Program size şifreli çıktıyı HEX formatında verir.</li>
</ol>

<h3>Şifre Çözme</h3>
<ol>
  <li>Menüden "2) Şifre Çöz" seçeneğini seçin.</li>
  <li>HEX formatındaki şifreli metni girin.</li>
  <li>Şifreleme sırasında kullanılan aynı kelimeyi girin.</li>
  <li>Program size çözülmüş metni gösterir.</li>
</ol>

<h2>Not</h2>
<p>
Bu proje basit bir metin şifreleme uygulamasıdır.
Gerçek güvenlik gerektiren ortamlarda kullanılmamalıdır.
</p>

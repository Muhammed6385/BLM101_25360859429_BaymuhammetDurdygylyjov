BLM101_25360859429_BaymuhammetDurdygylyjov

Ad: Baymuhammet 

Soyad: Durdygylyjov 

Öğrenci No: 25360859429 

Proje konusu: Aglar, Internet ve HTML 

Youtube link :

Proje açıklama:
Bu projenin amacı, Python kullanarak kullanıcıdan alınan bilgilerle basit bir kişisel web sayfası oluşturmaktır.
Kullanıcıdan alınan ad, biyografi ve ders bilgileri kullanılarak otomatik olarak bir HTML dosyası hazırlanır.

-----------------------------------------------------------------------------------

Kullanılan Araçlar ve Yapılar:

Bu projede harici bir kütüphane kullanılmamıştır. Python’un kendi hazır yapıları kullanılmıştır.

input() → Kullanıcıdan bilgi almak için kullanılmıştır.

split() → Dersleri virgüle göre ayırıp liste yapmak için kullanılmıştır.

for döngüsü → Dersleri tek tek HTML listesine eklemek için kullanılmıştır.

open() → HTML dosyası oluşturmak ve içine yazmak için kullanılmıştır.

f-string → Python değişkenlerini HTML kodunun içine eklemek için kullanılmıştır.

-----------------------------------------------------------------------------------

Programın Çalışma Mantığı:

Program çalıştığında ilk olarak kullanıcıdan adı, aldığı dersler ve kısa biyografisi istenir.
Dersler virgül ile ayrılmış şekilde alındığı için split(",") komutu kullanılarak dersler liste haline getirilir.

Daha sonra HTML sayfası için bir şablon hazırlanır.
Bu şablonun içine kullanıcının adı ve biyografisi eklenir.

Dersler listesi for döngüsü kullanılarak gezilir ve her ders <li> etiketi ile HTML listesine eklenir.
Bu sayede dersler alt alta düzgün bir şekilde gösterilir.

Son olarak hazırlanan HTML içeriği index.html adlı dosyaya yazılır.
Program bittiğinde kullanıcıya dosyanın başarıyla oluşturulduğu bilgisi verilir.

-----------------------------------------------------------------------------------

Algoritma Adımları:

1 Kullanıcıdan gerekli bilgiler alınır

2 Dersler liste haline getirilir

3 HTML içeriği hazırlanır

4 Dersler döngü ile HTML’ye eklenir

5 HTML dosyası oluşturulur

Sonucu bildir


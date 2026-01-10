# Kullanicidan ad bilgisi aliyorum
ad = input("Adiniz nedir? : ")

# Kullanicidan aldigi dersleri virgul ile ayirarak aliyorum
dersler = input("Aldiginiz dersleri virgul ile ayirarak yazin : ")

# Kullanicidan kisa bir biyografi aliyorum
biyografi = input("Kisa biyografinizi yazin:")

# Girilen dersleri virgulden ayirip liste haline getiriyorum
ders_listesi = dersler.split(",")

# HTML dosyasi icin baslangic icerigini olusturuyorum
# Ad ve biyografi bilgileri HTML icine ekleniyor
html_icerik = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>{ad} - Kisisel Sayfa</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }}
        h1 {{
            color: #2c3e50;
        }}
        p {{
            font-size: 16px;
        }}
        ul {{
            background-color: #ffffff;
            padding: 15px;
            border-radius: 5px;
        }}
        li {{
            color: #34495e;
        }}
    </style>
</head>
<body>

    <h1>{ad}</h1>

    <h2>Biyografi</h2>
    <p>{biyografi}</p>

    <h2>Aldigim Dersler</h2>
    <ul>
"""

# Ders listesindeki her dersi tek tek ekliyorum
for ders in ders_listesi:
    # strip ile bosluklari siliyorum
    html_icerik += f"<li>{ders.strip()}</li>\n"

# HTML kodunun kalan kismini kapatiyorum
html_icerik += """
    </ul>
    
</body>
</html>
"""

# index.html dosyasini yazmak icin aciyorum
with open("index.html", "w", encoding="utf-8") as dosya:
    dosya.write(html_icerik)

# Dosya olusturulduktan sonra ekrana bilgi yazdiriyorum
print("index.html basariyla olusturuldu!")

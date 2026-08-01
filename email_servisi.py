import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

TEST_MODU = True
BENIM_TEST_MAILIM = "aynur.sualp0907@gmail.com"

GONDERICI_MAIL = "aynur.sualp0907@gmail.com"
UYGULAMA_SIFRESI = os.environ.get('GMAIL_UYGULAMA_SIFRESI', '')

def musteriye_uyari_maili_gonder(musteri_ad, arac_plaka, kalan_km, musteri_gercek_email, sebep, durum):
    gidecek_adres = BENIM_TEST_MAILIM if TEST_MODU else musteri_gercek_email
    
    if durum == 'kritik':
        baslik_metni = "ACİL: Lastik Değişim Zamanı Geçti!"
        renk = '#dc3545'
    else:
        baslik_metni = "BİLGİLENDİRME: Lastik Değişim Zamanı Yaklaşıyor"
        renk = '#ffc107'

    if sebep == 'zaman':
        if durum == 'kritik':
            aciklama = "Aracınızın periyodik lastik değişim zamanı (geçmiş ortalamanıza göre) <b>geçmiştir</b>. Kilometre sınırınızı doldurmamış olsanız dahi, mevsimsel koşullar ve lastik ömrü gereği acilen değişim yapmanız gerekmektedir."
        else:
            aciklama = "Aracınızın periyodik lastik değişim zamanı yaklaşmaktadır. Mevsimsel veya dönemsel bakımınız için şimdiden planlama yapmanızı öneririz."
        km_bilgisi = ""

    else:
        if durum == 'kritik':
            aciklama = f"Sistemimizdeki yapay zeka analizine göre aracınızın lastik değişim kilometresi kritik seviyeye ulaşmıştır."
        else:
            aciklama = f"Sistemimizdeki yapay zeka analizine göre aracınızın lastik değişim kilometresine az kalmıştır."
        km_bilgisi = f"<li><b>Tahmini Kalan Kullanım:</b> {int(kalan_km)} KM</li>"


    mesaj_icerigi = f"""
<html>
    <body>
        <h2 style="color: {renk};">{baslik_metni}</h2>
        <p>Sayın <b>{musteri_ad}</b>,</p>
        <p><b>{arac_plaka}</b> plakalı aracınızla ilgili sistem uyarısı aşağıdadır:</p>

        <p style="font-size: 16px;">{aciklama}</p>
        <ul>
            {km_bilgisi}
        </ul>
        <p>Lütfen güvenliğiniz için en kısa sürede servisimizden randevu alınız.</p>
        <br>
        <p><i>Sağlıklı ve güvenli sürüşler dileriz.</i></p>
    </body>
</html>
"""
    
    msg = MIMEMultipart()
    msg['From'] = GONDERICI_MAIL
    msg['To'] = gidecek_adres
    msg['Subject'] = baslik_metni
    msg.attach(MIMEText(mesaj_icerigi, 'html', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GONDERICI_MAIL, UYGULAMA_SIFRESI)
        server.send_message(msg)
        server.quit()
        return True, gidecek_adres
    except Exception as e:
        print(f"Mail gönderme hatası: {e}")
        return False, str(e)
# 🚗 Lastik Takip ve Yapay Zeka Destekli Bakım Tahmin Sistemi

Bu proje, otomotiv servisleri ve lastik otelleri için geliştirilmiş, **Yapay Zeka (Random Forest Regressor)** destekli bir müşteri, araç ve işlem yönetim sistemidir. Sistem, müşterilerin geçmiş lastik değişim alışkanlıklarını analiz ederek bir sonraki değişimin ne zaman ve kaç kilometrede yapılacağını öngörür ve SMTP üzerinden proaktif E-posta bildirimleri (Uyarı/Kritik) gönderir.

## 🌟 Öne Çıkan Özellikler

- **🤖 Yapay Zeka Destekli Tahmin (Predictive Maintenance):** Scikit-Learn kütüphanesi kullanılarak eğitilen *Random Forest* modeli ile lastik ömrü tahmini. Model, araçların KM ve zaman (gün farkı) metriklerinden kullanım karakteristiğini (şahıs/ticari) örtülü olarak öğrenir.
- **📧 Otomatik E-posta Bildirimleri:** SMTP protokolü üzerinden, yapay zekanın tespit ettiği "Kritik" ve "Yaklaşıyor" durumlarına göre detaylı, HTML tabanlı otomatik bilgilendirme mailleri.
- **🛡️ Dinamik Veri ve Hata Yönetimi (Fault Tolerance):** Geriye dönük KM girişini engelleyen veri tabanı zırhı ve bilinmeyen serbest metin lastik tiplerini (Out of Distribution) modelin çökmesini engellemek için güvenli kategoride işleyen AI esnekliği.
- **📊 Excel Export & Raporlama:** Pandas ve OpenPyXL kullanılarak dinamik sütun genişlikleriyle otomatik formatlanan Müşteri ve İşlem Geçmişi raporları.
- **🔍 Gelişmiş UI/UX (Datalist):** Standart `select` yapıları yerine, binlerce kayıtta bile anında sonuç veren DOM destekli arama çubukları (Searchable Inputs) ve karanlık mod (Dark Mode) desteği.

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python 3.x, Flask, SQLite3
- **Data Science & AI:** Pandas, Scikit-Learn (Random Forest Regressor), Joblib
- **Frontend:** HTML5, Bootstrap 5, Jinja2, Vanilla JavaScript, SweetAlert2
- **Haberleşme:** smtplib (E-posta), python-dotenv (Çevre Değişkenleri Yönetimi)
- **Veri Dışa Aktarım:** io (BytesIO), OpenPyXL

## ⚙️ Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza klonlayın:
`git clone https://github.com/KULLANICI_ADINIZ/lastik-takip-sistemi.git`
`cd lastik-takip-sistemi`

2. Gerekli kütüphaneleri yükleyin:
`pip install flask pandas scikit-learn joblib openpyxl python-dotenv`

3. Çevresel değişkenleri (Environment Variables) ayarlayın:
Ana dizinde bir `.env` dosyası oluşturun ve E-posta için gereken SMTP ayarlarını yapılandırın (Detaylar için repodaki `.env.example` dosyasına bakabilirsiniz).

4. Sistemi başlatın:
`python app.py`

5. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin. 

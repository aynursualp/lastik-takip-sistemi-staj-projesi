import sqlite3
import pandas as pd
from lastik_kodlari import lastik_tipi_kodla
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
from datetime import datetime
import json

def veriler_getir():
    conn = sqlite3.connect('database.db')
    sorgu = "SELECT arac_id, islem_tarihi, kilometre, lastik_tipi FROM Islemler"
    df = pd.read_sql_query(sorgu, conn)
    conn.close()
    return df

islem_tablosu = veriler_getir()

islem_tablosu['lastik_tipi'] = islem_tablosu['lastik_tipi'].apply(lastik_tipi_kodla)

kodlanamayan_sayisi = islem_tablosu['lastik_tipi'.isna().sum()]
if kodlanamayan_sayisi > 0:
    print(f"UYARI: {kodlanamayan_sayisi} kayıt tanınmayan lastik tipi içerdiği için eğitimden çıkarıldı.")
islem_tablosu = islem_tablosu.dropna(subset=['lastik_tipi'])

islem_tablosu['islem_tarihi'] = pd.to_datetime(islem_tablosu['islem_tarihi'])
bugun = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))
islem_tablosu['gun_farki'] = (bugun - islem_tablosu['islem_tarihi']).dt.days

islem_tablosu = islem_tablosu.sort_values(by=['arac_id', 'islem_tarihi'])
islem_tablosu['hedef_km'] = islem_tablosu.groupby('arac_id')['kilometre'].shift(-1)
islem_tablosu['hedef_fark'] = islem_tablosu['hedef_km'] - islem_tablosu['kilometre']
islem_tablosu = islem_tablosu.dropna()

print("Veri seti hazırlandı (İlk 5 Satır): ")
print(islem_tablosu[['arac_id', 'kilometre', 'hedef_km', 'hedef_fark']].head())

y = islem_tablosu['hedef_fark'] #hedef
X = islem_tablosu.drop(['arac_id', 'islem_tarihi', 'hedef_km', 'hedef_fark'], axis=1) #girdi

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

tahminler = model.predict(X_test)
hata_payi = mean_absolute_error(y_test, tahminler)

print(f"Model Eğitildi! Ortalama Tahmin Hatası (Sapma): {hata_payi:.2f} Kilometre")

joblib.dump(model, 'lastik_tahmin_modeli.joblib')

model_bilgisi = {
    "mae": round(hata_payi, 2),
    "egitim_tarihi": datetime.today().strftime('%Y-%m-%d'),
    "veri_sayisi": len(islem_tablosu)
}

with open('model_bilgisi.json', 'w', encoding='utf-8') as f:
    json.dump(model_bilgisi, f, ensure_ascii=False)




import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON;")

c.execute('''CREATE TABLE IF NOT EXISTS Musteriler (
          musteri_id INTEGER PRIMARY KEY AUTOINCREMENT,
          ad TEXT,
          soyad TEXT,
          telefon TEXT,
          email TEXT)
          ''')

c.execute('''CREATE TABLE IF NOT EXISTS Araclar (
          arac_id INTEGER PRIMARY KEY AUTOINCREMENT,
          marka TEXT,
          model TEXT,
          plaka TEXT,
          musteri_id INTEGER,
          FOREIGN KEY (musteri_id) REFERENCES Musteriler(musteri_id) ON DELETE CASCADE)
          ''')

c.execute('''CREATE TABLE IF NOT EXISTS Islemler (
          islem_id INTEGER PRIMARY KEY AUTOINCREMENT,
          arac_id INTEGER,
          islem_tarihi TEXT,
          kilometre INTEGER,
          lastik_tipi TEXT,
          FOREIGN KEY (arac_id) REFERENCES Araclar(arac_id) ON DELETE CASCADE)
          ''')

conn.commit()
conn.close()
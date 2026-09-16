import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_YOLU = os.path.join(BASE_DIR, 'database.db')

conn = sqlite3.connect(DB_YOLU)
c = conn.cursor()

try:
    c.execute("ALTER TABLE Musteriler ADD COLUMN email TEXT")
except Exception as e:
    print(f"Hata oluştu: {e}")

conn.commit()
conn.close()
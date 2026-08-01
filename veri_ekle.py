import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''INSERT INTO Musteriler (ad, soyad, telefon) VALUES (?, ?, ?)''', ('Ahmet', 'Yılmaz', '05051234567'))
    c.execute('''INSERT INTO Musteriler (ad, soyad, telefon) VALUES (?, ?, ?)''', ('Ayşe', 'Kara', '05059876543'))
    c.execute('''INSERT INTO Musteriler (ad, soyad, telefon) VALUES (?, ?, ?)''', ('Mehmet', 'Demir', '05057654321'))
    conn.commit()
    conn.close()

create_database()
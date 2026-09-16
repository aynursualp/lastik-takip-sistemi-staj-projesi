lastik_tipi_kodlari = {
        'YAZ': 0,
        'KIS': 1,
        '4 MEVSIM': 2, 
        'DIGER': 3
    }

def lastik_tipi_kodla(deger):
        if not deger:
            return None
        
        normalize = deger.strip().upper()
        normalize = normalize.replace('İ', 'I').replace('Ş', 'S').replace('Ğ', 'G').replace('Ü', 'U').replace('Ö', 'O').replace('Ç', 'C')

        if normalize == 'YAZ':
            return lastik_tipi_kodlari['YAZ']
        elif normalize == 'KIS':
            return lastik_tipi_kodlari['KIS']
        elif normalize in ('4 MEVSIM', '4MEVSIM', 'DORT MEVSIM'):
            return lastik_tipi_kodlari['4 MEVSIM']
        else:
            return lastik_tipi_kodlari['DIGER']
        
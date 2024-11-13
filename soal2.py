tahun = int(input("MASUKAN TAHUN NYAAAAA: "))

def kabisat (tahun):
    if tahun % 400 == 0:
        return True

    elif tahun % 4 == 0 and tahun % 100 != 0:
        return True

    else:
        return False     

print('='*50)
if kabisat(tahun):
    print(f"{tahun} merupakan TAHUN KABISAT UHUYYY.")
else:
    print(f"{tahun} BUKAN TAHUN KABISATT WOYYYYYY.")

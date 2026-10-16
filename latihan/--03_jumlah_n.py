# Program: 03_jumlah_n.py
# Deskripsi: Menghitung jumlah deret 1 sampai n menggunakan perulangan dalam fungsi.

def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(jumlah_n(10))
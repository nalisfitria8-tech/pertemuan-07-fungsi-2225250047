# Program: 05_scope.py
# Deskripsi: Eksperimen scope variabel global dan lokal.

x = 10

def demo(x):
    y = x + 5
    print("di dalam fungsi:", x, y)
    return y

hasil = demo(20)
print("di luar fungsi:", x, hasil)
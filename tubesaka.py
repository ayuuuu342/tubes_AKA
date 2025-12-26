import time
import sys
import matplotlib.pyplot as plt


# Tingkatkan batas rekursi
sys.setrecursionlimit(50000)

# METODE ITERATIF
def balik_iteratif(arr):
    hasil = arr[:]
    kiri = 0
    kanan = len(arr) - 1
    
    while kiri < kanan:
        hasil[kiri], hasil[kanan] = hasil[kanan], hasil[kiri]
        kiri += 1
        kanan -= 1
    
    return hasil

# METODE REKURSIF
def balik_rekursif(arr):
    hasil = arr[:]
    
    def rekursi(kiri, kanan):
        if kiri >= kanan:
            return
        hasil[kiri], hasil[kanan] = hasil[kanan], hasil[kiri]
        rekursi(kiri + 1, kanan - 1)
    
    rekursi(0, len(arr) - 1)
    return hasil

# WAKTUNYA
def ukur_waktu(fungsi, arr):
    try:
        waktu_mulai = time.perf_counter()
        hasil = fungsi(arr)
        waktu_selesai = time.perf_counter()
        waktu_ms = (waktu_selesai - waktu_mulai) * 1000
        return waktu_ms, True
    except RecursionError:
        return 0, False

# TABELNYA
ukuran_array = [1, 5, 10, 100, 1000, 5000, 10000, 50000]
hasil = []

for ukuran in ukuran_array:
    arr = list(range(1, ukuran + 1))
    
    # Iteratif
    waktu_iter, sukses_iter = ukur_waktu(balik_iteratif, arr)
    
    # Rekursif
    waktu_rek, sukses_rek = ukur_waktu(balik_rekursif, arr)
    
    if sukses_iter and sukses_rek:
        hasil.append([ukuran, waktu_rek, waktu_iter])

print("\n" + "+" + "="*12 + "+" + "="*25 + "+" + "="*25 + "+")
print(f"| {'n':^10} | {'Waktu Rekursif (ms)':^23} | {'Waktu Iteratif (ms)':^23} |")
print("+" + "="*12 + "+" + "="*25 + "+" + "="*25 + "+")

for data in hasil:
    ukuran, waktu_rek, waktu_iter = data
    print(f"| {ukuran:>10} | {waktu_rek:>23.6f} | {waktu_iter:>23.6f} |")
    print("+" + "-"*12 + "+" + "-"*25 + "+" + "-"*25 + "+")

# INI UNTUK GRAFIK YAAAAKKKKK   
ukuran_list = [data[0] for data in hasil]
waktu_rek_list = [data[1] for data in hasil]
waktu_iter_list = [data[2] for data in hasil]

# BUAT LINE CHART KAKAKK    
plt.figure(figsize=(10, 6))
plt.plot(ukuran_list, waktu_rek_list, marker='o', linewidth=2, 
         markersize=8, label='Rekursif', color="#92396A")
plt.plot(ukuran_list, waktu_iter_list, marker='s', linewidth=2, 
         markersize=8, label='Iteratif', color='#3498db')

plt.xlabel('Ukuran Array (n)', fontsize=12, fontweight='bold')
plt.ylabel('Waktu Eksekusi (ms)', fontsize=12, fontweight='bold')
plt.title('Perbandingan Waktu Eksekusi: Iteratif vs Rekursif', 
          fontsize=14, fontweight='bold', pad=20)
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()

# BUAT NAMPILIN GRAFIK DEHHHHH
plt.show()
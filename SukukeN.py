print("Program Hitung Suku Ke-N")

nilaiAwal = float(input("Masukan Suku Pertama :"))
beda = float(input("Masukan Beda :"))
N = int(input("Masukan Suku ke-N :"))

suku   = nilaiAwal + (N - 1) * beda
jumlah = N/2 * (nilaiAwal + suku)

print("Suku ke-", N, "adalah", suku)
print("Jumlah dari suku ke-", N, "adalah", jumlah)
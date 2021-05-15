print("Latihan Percabanga")

Nilai = int(input("Masukan Nilai Siswa :"))

if (Nilai <= 30) :
	print("Anda Mendapat Nilai D")

elif (Nilai <= 60):
	print("Anda Mendapat Nilai C")

elif (Nilai >= 70 and Nilai <= 85):
	print("Anda Mendapat Nilai B")

elif (Nilai >= 90 and Nilai <= 100):
	print("Anda Mendapat Nilai A")

else :
	print("Harap Memasukan angka range 0 - 100")
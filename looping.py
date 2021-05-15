import os
os.system("clear")
print("Latihan Looping")

print("1.While\n2.For\n3.Nested Looop")
pil = int(input("Masukan Pilihan :"))

if (pil == 1) :
	print("\n\t\tPerulangan While\n")
	angka  =int(input("Masukan Angka Pertama :"))
	banyak =int(input("Masukan Banyak Looping:"))

	while angka <= banyak:
		print("angka", angka)
		angka = angka + 1

elif (pil == 2):
	print("\n\t\tPerulangan for\n")
	angka  = int(input("Masukan Angka Pertama :"))
	banyak = int(input("Masukan Banyak Looping:"))

	for angka in range(banyak):
		print("angka ke-", angka)

elif (pil == 3):
	print("\n\t\tNested Loop")
	print("\tMenampilkan segitiga bintang\n")
	for baris in range(5):
		for kolom in range(baris+1):
			print("*" , end=" ")
		print()




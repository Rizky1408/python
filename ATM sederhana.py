import os
os.system("clear")

print("\t==============================")
print("\t         Program ATM\n")
print("\t        Pecahan 5000\n")
print("\t  Design by Rizky Adi Ryanto\n")
print("\t==============================")
print("^Selamat Datang Di ATM^\n\n")

kode  = 12345
saldo = 500000
pin = int(input("Masukan PIN ATM Anda :"))

if (pin == kode ):
	print("1.Tarik Tunai\n2.Transfer\n3.Cek Saldo")
	menu = int(input("Masukan Pilihan :"))
	if (menu == 1) :
		jumlah = float(input("Masukan Jumlah Yang ingin di tarik :"))
		if (jumlah >= saldo or jumlah >= saldo - 50000) :
			print("Saldo Anda Tidak Mencukupi")
		elif (jumlah < saldo) :
			hasil = saldo - jumlah
			print("Terimakasih Telah Bertransaksi")
			print("Saldo Anda sekarang", hasil)

	elif (menu == 2) :
		nomor  = int(input("Masukan Nomor Rekening yang di tuju :"))
		banyak = float(input("Masukan Jumlah yang ingin anda kirim :"))
		print("\n")
		print("No rek :", nomor)
		print("Jumlah :", banyak)
		confir = input("Apakah Sudah Benar(y/t) :")
		if (confir == "y" or confir == "Y") :
			if (banyak < saldo - 50000) :
				transf = saldo - banyak	
				print("Transaksi Berhasil,Saldo anda sekarang", transf)
			else :
				print("Saldo Anda Tidak Mencukupi")
			
		elif (confir == "t" or confir == "T") :
			print("Harap Ulangi Dari Awal")
		else :
			print("Inputan salah -_-")
	
	elif (menu == 3) :
		print("Saldo Anda Sekarang ", saldo)

	else :
		os.system("clear")
		print("Warning! Inputan Salah")
elif (pin != kode) :
	print("Warning! Inputan Salah")
		


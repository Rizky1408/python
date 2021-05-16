import os
os.system("clear")
print("Program Konvert Uang per Lembar")

uang = int(input("Masukan Jumlah Uang :"))

a = int(uang / 100000)
sisa = uang % 100000
b = int(sisa / 50000)
sisa =  sisa % 50000
c = int(sisa / 20000)
sisa = sisa % 20000
d = int(sisa / 10000)
sisa = sisa % 10000
e = int(sisa / 5000)
sisa = sisa % 5000
f = int(sisa / 2000)
sisa = sisa % 2000
g = int(sisa / 1000)
sisa = sisa % 1000
h = int(sisa / 500)
sisa = sisa % 500
i = int(sisa / 200)
sisa = sisa % 200
j = int(sisa / 100)
sisa = sisa % 100
hasil1 = int(a + b + c + d + e + f + g)
hasil2 = int(h + i + j)
print("Uang 100000 ada", a, "Lembar")
print("Uang 50000  ada", b, "Lembar")
print("Uang 20000  ada", c, "Lembar")
print("Uang 10000  ada", d, "Lembar")
print("Uang 5000   ada", e, "Lembar")
print("Uang 2000   ada", f, "Lembar")
print("Uang 1000   ada", g, "Lembar")
print("Uang 500    ada", h, "Lembar")
print("Uang 200    ada", i, "Lembar")
print("Uang 100    ada", j, "Lembar")
print("Jumlah Uang Lembar adalah", hasil1, "Lembar")
print("Jumlah Uang Koin adalah", hasil2, "Keping")
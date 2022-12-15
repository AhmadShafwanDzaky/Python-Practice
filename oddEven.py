genap = -1
ganjil = 0
i = 1
while i >= 1:
    i = int(input("Masukkan angka : "))
    if i%2 == 0:
        genap += 1
    elif i%2 == 1:
        ganjil += 1
    elif i == 0:
        break

print("Jumlah bilangan genap : ", genap)
print("Jumlah bilangan ganjil : ", ganjil)
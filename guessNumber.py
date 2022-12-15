import random
print("=" * 55)
print("Selamat datang di game tebak angka Jaki!")
print("Kamu memiliki 3 kali kesempatan untuk menebak angka")
print("=" * 55)

while True:
    start = input("Enter untuk memulai gamenya")
    if start == "":
        while True:
            topRange = input("Masukkan batas angka terbesar untuk ditebak : ")
            if topRange.isdigit():
                topRange = int(topRange)
                break
            else:
                print("Masukkan angka!!")
                continue      

        number = random.randint(1, topRange)

        for i in range(0, 3):
            myNumber = int(input("Masukkan angka tebakan kamu : "))
            if myNumber == number:
                print("Tebakan kamu benar!!!")
                break
            elif myNumber < number:
                print("Tebakan kamu terlalu kecil!!!")
                continue
            elif myNumber > number and myNumber < topRange:
                print("Tebakan kamu terlalu besar!!!")
                continue
            elif myNumber > topRange:
                print("Masukkan angka dari 1-", topRange)
                continue
        while True:
            again = input("Masih mau main gamenya? (y/n): ")
            if again == "y":
                break
            elif again == "n":
                quit()
            else:
                print("Masukkan y/n !!!")
                continue
    else:
        print("Enter untuk memulai!!!")
        continue
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

        myNumber = int(input("Masukkan angka kamu yang bakal ditebak : "))

        for i in range(0, 3): 
            number = random.randint(1, topRange)
            if myNumber == number:
                print("Tebakan komputer benar!!!")
                break
            elif myNumber > number:
                print("\nTebakan komputer terlalu kecil!!!")
                print("Tebakan komputer : ", number)
                continue
            elif myNumber < number and myNumber < topRange:
                print("\nTebakan komputer terlalu besar!!!")
                print("Tebakan komputer : ", number)
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
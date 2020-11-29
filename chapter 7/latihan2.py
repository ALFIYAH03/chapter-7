print('Latihan 2 Chapter 7')
try:
    selesai = False
    while not(selesai):
        menambahData= str(input('Data yang ditambahkan:'))
        file = open("D:/Apheint/PROTEK/chapter 7/dataMhs.txt", "a")
        file.write("(0)\n". format(menambahData))
        file.close()

        choice = None

        while choice not in("y", "n"):
            choice = str(input("Mau lagi (y/n):"))
            if(choice=='y'):
               selesai=False
            elif(choice=='n'):
                selesai=True
            else:
                print('Masukkan kembali pilihan (y/n)')

except FileNotFoundError:
    print('File tidak ditemukan')


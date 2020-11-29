try :
    file = open("D:/Apheint/PROTEK/chapter 7/data.txt", "r")
    sum = 0
    for data in file :

        try :
            sum = sum + int(data)
            print(sum)

        except ValueError:
            print('Tipe data tidak valid')

except FileNotFoundError :
    print('File tidak ditemukan')

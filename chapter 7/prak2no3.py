#membuka dan membaca file d:/ data.txt
file = open ("c:/data.txt", "r")

#baca baris pertama dari file
#simpan ke dalam variabel bill sbg integer
bil1 = int(file.readline())

#baca baris pertama dari file
#simpan ke dalam variabel bill sbg integer
bil2 = int(file.readline())

#hitung dan tampilkan hasil bagi
hasil = bil1/bil2
print(bil1, ' dibagi ' , bil2 ,' sama dengan ' , hasil )

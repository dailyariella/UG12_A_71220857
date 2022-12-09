pisah_angka = int(input("Masukkan Pembatas : "))
angka_dilarang = int(input("Masukkan angka terlarang : "))
for i in range(pisah_angka):
    if i == angka_dilarang:
        continue
    print(i,end=" ")
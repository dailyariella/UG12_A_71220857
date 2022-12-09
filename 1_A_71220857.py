pertama = int(input("Masukkan awal deret:"))
kedua = int(input("Masukkan akhir deret:"))
for i in range(pertama,kedua):
    if i%2 == 1 and i%3!= 0 and i%6!= 0:
        print(i,end=" ")
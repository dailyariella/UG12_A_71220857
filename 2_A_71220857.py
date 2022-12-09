masukkan_pernyataan = input("Masukkan nama : ")
timbul = 0
for i in range(len(masukkan_pernyataan)):
    timbul +=1
    print(masukkan_pernyataan[:timbul])
for i in range(len(masukkan_pernyataan)):
    timbul -=1
    print(masukkan_pernyataan[:timbul])    
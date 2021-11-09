b=0
c=0
# kullanıcıdan bir tam sayı girmesini istiyoruz.
sayi=int(input("Bir tam sayı giriniz: "))
# girilen sayıya kadar olan sayılarla işlem yapması için for döngüsüne alıyoruz.
for i in range(2,sayi+1):
    for b in range(2,i):
        c=0
# asal sayı bulmanın tam tersini yaparak istediğimiz sonucu alıyoruz.
        if i%b == 0:
            c=1
            break
    if c==1:
        print(i)
        
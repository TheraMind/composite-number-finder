b=0
c=0
sayi=int(input("Bir tam sayı giriniz: "))
for i in range(2,sayi+1):
    for b in range(2,i):
        c=0
        if i%b == 0:
            c=1
            break
    if c==1:
        print(i)
        

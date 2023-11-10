bilangan = int(input("Masukkan bilangan: "))
i = 2
while i < bilangan:
    if bilangan % i == 0:
        print(bilangan, "bukan bilangan prima.")
        break
    i += 1
else:
    print(bilangan, "adalah bilangan prima.")
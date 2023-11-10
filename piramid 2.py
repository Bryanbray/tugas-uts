tinggi = int(input("masukan tinggi: "))

for i in range(tinggi):
    for k in range(2 * i + 1):
        print('*', end='')   
    for j in range(tinggi - i - 1):
        print(' ', end='')
    print()
bilangan = int(input("angka disini: "))
a = bilangan

for i in range (a, 0, -1):
    if a % i == 0:
        print(i)


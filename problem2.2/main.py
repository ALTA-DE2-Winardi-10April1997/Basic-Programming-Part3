bilangan = int(input())

for x in range(bilangan+1, 0, -1):
    if bilangan % x == 0:
        print(x)
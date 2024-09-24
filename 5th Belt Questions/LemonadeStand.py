a = int(input())
b = list(map(int, input().split()))

fives = 0
tens = 0

for i in b:
    if i == 5:
        fives += 1
    elif i == 10:
        if fives == 0:
            print("False")
            break
        else:
            fives -= 1
            tens += 1
    elif i == 20:
        if tens > 0 and fives > 0:
            tens -= 1
            fives -= 1
        elif fives >= 3:
            fives -= 3
        else:
            print("False")
            break

else:
    print("True")


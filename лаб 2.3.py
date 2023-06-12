x = int(input())
while x < 1000000000:
    if x == 1:
        break
    else:
        x *= x
        print(x)
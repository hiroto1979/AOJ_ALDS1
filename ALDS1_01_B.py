def gcd(x, y):
    if x < y:
        x, y = y, x
    while True:
        if x % y == 0:
            break
        x, y = y, x % y
    print(y)

if __name__ == '__main__':
    x, y = [int(i) for i in input().split()]
    gcd(x, y)

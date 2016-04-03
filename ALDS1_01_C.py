import math

def is_prime(i):
    if i == 2 or i == 3:
        return 1
    elif i % 2 == 0:
        return 0
    else:
        for j in range(3, int(math.sqrt(i))+1,2):
            if i % j == 0:
                return 0
        return 1

if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for i in range(n):
        j = int(input())
        cnt += is_prime(j)
        # print(cnt)
    print(cnt)

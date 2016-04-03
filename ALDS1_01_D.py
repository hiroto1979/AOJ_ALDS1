def maximum_profit(n, l):
    maximum = -(10 ** 9)
    inf = l[0]
    for i in range(1, n):
        if maximum < l[i] - inf:
            maximum = l[i] - inf
        if l[i] < inf:
            inf = l[i]
    print(maximum)

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))

    maximum_profit(n, l)

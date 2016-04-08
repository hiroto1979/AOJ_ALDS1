def allocation_check(n, k, p, containers):
    i = 0
    for j in range(k):
        s = 0
        while s + containers[i] <= p:
            s = s + containers[i]
            i += 1
            if i == n:
                return n
    return i

def allocation_solve(n, k, containers):
    left = 0
    right = 100000 * 10000 # 個数と荷物の重量の最大値
    while 1 < right - left:
        mid = (right + left) // 2
        v = allocation_check(n, k, mid, containers)
        if v >= n:
            right = mid
        else:
            left = mid
    return right


if __name__ == '__main__':
    n, k = [int(i) for i in input().split()]
    containers = []
    for i in range(n):
        containers.append(int(input()))
    print(allocation_solve(n, k, containers))

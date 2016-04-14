def solve():
    ans = 0

    B = A[:]
    V = [False] * n

    B.sort()
    for i in range(n):
        T[B[i]] = i
    for i in range(n):
        if V[i]:
            continue
        cur = i
        S = 0
        m = max(A) + 1
        an = 0
        while True:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]: break
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)
    return ans


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    s = min(A)
    T = [0] * (max(A)+1)
    ans = solve()
    print(ans)

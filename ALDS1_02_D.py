def insertion_sort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while 0 <= j and v < A[j]:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v
    return cnt

def shell_sort(A, n):
    # g = G[i]の選び方は様々ではある。
    # g[n+1] = 3 * g[n] + 1 の数列を用いると、
    # 計算量がO(N^1.25)になると予測されているため、これを用いる。
    # なお、g = 1までにソートの対象にならない要素が
    # 多く発生してしまうような数列を用いても、
    # 効率化が期待できないことに注意すること。
    G = []
    g = 1
    while g <= n // 3 + 1:
        G.append(g)
        g = 3 * g + 1
    G = G[::-1]
    m = len(G)
    print(m)
    print(" ".join(map(str,G)))
    cnt = 0
    for i in range(m):
        cnt += insertion_sort(A, n, G[i])
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    shell_sort(A, N)
    for i in A:
        print(i)

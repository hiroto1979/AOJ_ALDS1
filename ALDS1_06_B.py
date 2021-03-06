def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

if __name__ == '__main__':
    r = int(input())
    A = [int(i) for i in input().split()]
    q = partition(A, 0, r-1)

    A[q] = "[{}]".format(A[q])
    print(" ".join(map(str,A)))
def insert_sort(A, N):
    for i in range(N):
        v = A[i]
        j = i - 1
        while 0 <= j and v < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(" ".join(map(str, A)))

if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]

    insert_sort(A, N)

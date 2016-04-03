def selection_sort(A, N):
    cnt = 0
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if A[i] != A[minj]:
            A[i], A[minj] = A[minj], A[i]
            cnt += 1
    print(" ".join(map(str,A)))
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]

    selection_sort(A, N)

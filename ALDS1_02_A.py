def bubble_sort(A, N):
    cnt = 0
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                cnt += 1
                flag = True
    print(" ".join(map(str,A)))
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]

    bubble_sort(A, N)

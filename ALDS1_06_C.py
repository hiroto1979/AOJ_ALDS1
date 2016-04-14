def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def check_stablity(A):
    for i in range(1, len(A)):
        if A[i-1][1] == A[i][1]:
            if A[i-1][2] > A[i][2]:
                return "Not stable"
    return "Stable"


if __name__ == '__main__':
    n = int(input())
    A = []
    for i in range(n):
        suit, num = input().split()
        A += [[suit, int(num), i]]
    quicksort(A, 0, n-1)
    print(check_stablity(A))

    for i in A:
        print(i[0], i[1])

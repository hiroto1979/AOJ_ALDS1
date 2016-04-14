def counting_sort(A, B, k):
    C = [0 for i in range(k+1)]
    # C[i] に i の出現数を記録する
    for j in range(len(A)):
        C[A[j]] += 1
    # C[i] に i 以下の数の出現数を記録する
    for i in range(1, k+1):
        C[i] += C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [0 for i in range(n)]
    counting_sort(A, B, max(A))
    print(" ".join(map(str,B)))
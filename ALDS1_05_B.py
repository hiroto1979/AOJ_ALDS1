def merge(A, left, mid, right):
    global cnt
    SENTINEL = 10 ** 9 + 1
    L = A[left:mid] + [SENTINEL]
    R = A[mid:right] + [SENTINEL]
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    cnt += right - left

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    cnt = 0
    merge_sort(A, 0, len(A))
    print(' '.join(map(str, A)))
    print(cnt)

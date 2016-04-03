def bubble_sort(C, N):
    A = C[:]
    for i in range(0, N):
        for j in range(N-1, i, -1):
            if int(A[j][1]) < int(A[j-1][1]):
                A[j], A[j-1] = A[j-1], A[j]
    return A

def selection_sort(C, N):
    A = C[:]
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i], A[minj] = A[minj], A[i]
    return A

# 常に安定なソートを行うバブルソートと比較を行うことにより、
# 選択ソートが安定かどうかを判定する。
def is_selection_stability(C, N):
    C1 = C[:]
    C2 = C[:]
    if bubble_sort(C1, N) == selection_sort(C2, N):
        return "Stable"
    else:
        return "Not stable"

if __name__ == '__main__':
    N = int(input())
    C = [i for i in input().split()]

    C1 = C[:]
    print(" ".join(bubble_sort(C1, N)))
    # バブルソートは常に安定なソートのため、
    # 常に「Stable」を出力する。
    print("Stable")

    C2 = C[:]
    print(" ".join(selection_sort(C2, N)))
    print(is_selection_stability(C2, N))

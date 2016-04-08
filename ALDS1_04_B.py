def binary_search(S, key):
    left = 0
    right = len(S)
    while left < right:
        mid = (left + right) // 2
        # print("left:" + str(left) + " right:" + str(right) + " mid:" + str(mid))
        # print("S[mid]:" + str(S[mid]) + " key:" + str(key))
        if S[mid] == key:
            return 1
        elif S[mid] > key:
            right = mid
        elif S[mid] < key:
            left = mid + 1
    return 0


if __name__ == '__main__':
    n = int(input())
    S = [int(i) for i in input().split()]

    q = int(input())
    T = [int(i) for i in input().split()]
    C = 0
    for i in T:
        C += binary_search(S, i)
    print(C)

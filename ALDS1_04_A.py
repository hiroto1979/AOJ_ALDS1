def linear_search(S, key):
    for i in range(len(S)):
        if S[i] == key:
            return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    S = [int(i) for i in input().split()]

    q = int(input())
    T = [int(i) for i in input().split()]
    C = 0
    for i in T:
        C += linear_search(S, i)
    print(C)
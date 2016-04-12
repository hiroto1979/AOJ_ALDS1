from itertools import combinations

def exhaustive_search(n, A_i):
    numbers = set()
    for i in range(1, n+1):
        for c in combinations(A_i, i):
            numbers.add(sum(c))
    return numbers


if __name__ == '__main__':
    n = int(input())
    A_i = [int(i) for i in input().split()]
    numbers = exhaustive_search(n, A_i)

    q = int(input())
    m_i = [int(i) for i in input().split()]
    for m in m_i:
        if m in numbers:
            print("yes")
        else:
            print("no")
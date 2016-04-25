def reconst(l, r):
    global pos
    if l >= r:
        return
    c = pre[pos]
    pos += 1
    m = ino.index(c)
    reconst(l, m)
    reconst(m+1, r)
    A.append(c)

if __name__ == "__main__":
    n = int(input())
    pre = [int(i) for i in input().split()]
    ino = [int(i) for i in input().split()]

    pos = 0
    A = []
    reconst(0, n)
    print(" ".join(map(str,A)))

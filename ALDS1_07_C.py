class Node():
    def __init__(self):
        self.p = -1
        self.l = 0
        self.r = 0

def pre_parse(u):
    if u == -1:
        return
    print(" " + str(u), end = "")
    pre_parse(tree[u].l)
    pre_parse(tree[u].r)

def in_parse(u):
    if u == -1:
        return
    in_parse(tree[u].l)
    print(" " + str(u), end = "")
    in_parse(tree[u].r)

def post_parse(u):
    if u == -1:
        return
    post_parse(tree[u].l)
    post_parse(tree[u].r)
    print(" " + str(u), end = "")


if __name__ == "__main__":
    n = int(input())
    tree = [None for i in range(n)]
    for i in range(n):
        tree[i] = Node()
    for i in range(n):
        v, l, r = [int(i) for i in input().split()]
        tree[v].l = l
        tree[v].r = r
        if l != -1:
            tree[l].p = v  
        if r != -1:
            tree[r].p = v

    for i in range(n):
        if tree[i].p == -1:
            root = i

    print("Preorder")
    pre_parse(root)
    print()
    print("Inorder")
    in_parse(root)
    print()
    print("Postorder")
    post_parse(root)
    print()
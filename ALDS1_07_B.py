class Node():
    def __init__(self, node_id, left, right):
        self.node_id    =   node_id
        self.parent     =   -1
        self.sibling    =   -1
        self.left       =   left
        self.right      =   right
        self.degree     =   0
        self.depth      =   0
        self.height     =   0
        self.tp        =   "leaf"

def printing(tree):
    # parent・sibling・degreeの設定
    for node in tree:
        if node.left != -1:
            tree[node.left].parent = node.node_id
            tree[node.left].sibling = node.right
            tree[node.node_id].degree += 1
        if node.right != -1:
            tree[node.right].parent = node.node_id
            tree[node.right].sibling = node.left
            tree[node.node_id].degree += 1

    # height・depth・tpの設定
    for node in tree:
        # heightの設定
        set_height(tree, node.node_id)
        # depthの設定
        p = node.parent
        while p != -1:
            p = tree[p].parent
            node.depth += 1
        # tpの設定
        if node.parent == -1:
            node.tp = "root"
        elif node.height != 0:
            node.tp = "internal node"

    # 表示
    for node in tree:
        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node.node_id, node.parent, node.sibling, node.degree, node.depth, node.height, node.tp))

def set_height(tree,u):
    h1 = h2 = 0
    if tree[u].right != -1:
        h1 = set_height(tree, tree[u].right) + 1
    if tree[u].left != -1:
        h2 = set_height(tree, tree[u].left) + 1
    tree[u].height = max(h1, h2)
    return tree[u].height


if __name__ == '__main__':
    n = int(input())
    tree = [None for i in range(n)]

    for i in range(n):
        node = [int(i) for i in input().split()]
        tree[node[0]] = Node(node[0], node[1], node[2])

    printing(tree)

class Node():
    def __init__(self, node_id, children):
        self.node_id  = node_id
        self.parent   = -1
        self.depth    = 0
        self.tp       = "root"
        self.children = children

def printing(tree):
    # parentの設定
    for node in tree:
        if node.children != []:
            for c in node.children:
                tree[c].parent = node.node_id

    # tpとdepthの設定
    for node in tree:
        # tpの設定
        if node.children == [] and node.parent != -1:
            node.tp = "leaf"
        elif node.children != [] and node.parent != -1:
            node.tp = "internal node"
        # depthの設定
        p = node.parent
        while p != -1:
            p = tree[p].parent
            node.depth += 1
    # for node in tree:
    #    print(node.children)
    #    print(str(node.node_id) + " : " + str(node.parent) + " : " + str(node.tp) + " : " + str(node.depth))

    # 表示
    for node in tree:
        print("node {}: parent = {}, depth = {}, {}, {}".format(node.node_id, node.parent, node.depth, node.tp, node.children))


if __name__ == '__main__':
    n = int(input())
    tree = [None for i in range(n)]
    for i in range(n):
        node = [int(i) for i in input().split()]
        tree[node[0]] = Node(node[0], node[2:])
        # print(tree[node[0]].children)

    printing(tree)

# パフォーマンス上の問題より、listではなく、dequeを用いた実装を採用する。
# 
# 【参考１】ドキュメントにおけるDequeの説明
# http://docs.python.jp/3.5/library/collections.html#collections.deque
# Deque とは、スタックとキューを一般化したものです。
# Deque はどちらの側からも append と pop が可能で、スレッドセーフでメモリ効率がよく、
# どちらの方向からもおよそ O(1) のパフォーマンスで実行できます。
# list オブジェクトでも同様の操作を実現できますが、
# これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような
# pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします。
# 
# 【参考２】ベンチマーク的な要素は以下URLに詳しい。
# http://x1.inkenkun.com/archives/944

from collections import deque

def doubly_linked_list(n):
    queue = deque()
    for i in range(n):
        command = input().split()
        if command[0] == "insert":
            queue.appendleft(command[1])
        elif command[0] == "delete":
            try:
                queue.remove(command[1])
            except:
                pass
        elif command[0] == "deleteFirst":
            queue.popleft()
        elif command[0] == "deleteLast":
            queue.pop()
        # print(queue)
    print(" ".join(map(str,queue)))

if __name__ == '__main__':
    n = int(input())
    doubly_linked_list(n)

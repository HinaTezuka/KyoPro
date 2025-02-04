""" 書き方１ """

# Nodeという名前のクラスを定義します。これはリストの各要素（ノード）を表現します。
class Node:
    # ノードはデータを持ち、次のノードへの参照（リンク）を持つことができます。
    def __init__(self,data):
        # データ部分には任意の値を格納できます。
        self.data = data
        # next属性は次のノードへのリンクを格納します。初期状態ではNone（つまりリンクが存在しない）です。
        self.next = None

# SinglyLinkedListという名前のクラスを定義します。これは片方向リスト全体を表現します。
class SinglyLinkedList:
    # リストは最初のノード（head）を持つことができます。
    def __init__(self, node):
        # リストの先頭を定義します。
        self.head = node

# データとして4、65、24を持つ3つのノードを作成します。
node1 = Node(4)
node2 = Node(65)
node3 = Node(24)

# 新しい片方向リストを作成し、その先頭ノードとしてnode1を指定します。
numList = SinglyLinkedList(node1)

# node1の次のノードとしてnode2を、node2の次のノードとしてnode3を指定します。
# これにより、3つのノードが連結リストとしてつながります。
# 注意: ここでの=演算子は、新たな値を割り当てるのではなく、メモリ上の場所（参照）を指定します。
numList.head.next = node2
numList.head.next.next = node3

# 連結リストを反復して各ノードのデータを出力します。
# 'currentNode'は現在見ているノードを指し、各反復ごとに次のノードを指すよう更新されます。
# これを、次のノードが存在しなくなる（Noneになる）まで続けます。
currentNode = numList.head
while currentNode is not None:
    # 現在のノードのデータを出力します。
    print(currentNode.data)
    # 現在のノードを次のノードに更新します。
    currentNode = currentNode.next

""" 書き方2 """

""" 
Nodeの構造
データが入る変数と次のオブジェクトを指すポインターを準備します。
このクラスを利用して連結リストを作っていきます。 
"""
from typing import Any
class Node(object):
    def __init__(self, data: Any, next_node: Node = None):
        self.data = data # データ
        self.next = next_node # 次のNodeを指す参照変数(ポインタ)

"""
連結リストの初期化
連結リストのクラスを作成して、先頭にNoneを追加しておきます。
この状況はLinkedListをインスタンス化した場合にデータが何も入っていない状態と同じです。
"""
class LinkedList(object):
    def __init__(self, head = None) -> None:
        self.head = head # インスタンス化した時にNoneをいれておく。
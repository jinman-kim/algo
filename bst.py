class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insert(self, data, method='iterative'):
        if method in 'recursion':
            self.__root = self._insert_rec(self.__root, data)
        else:
            self._insert_iter(data)

    def _insert_rec(self, node, data):
        if not node:
            node = Node(data)
        else:
            if node.data > data:
                node.left = self._insert_rec(node.left, data)
            else:
                node.right = self._insert_rec(node.right, data)

    def _insert_iter(self, data):
        if not self.__root:
            self.__root = Node(data)
            return

        new_node = Node(data)

        curr = self.__root
        parent = None

        while (curr != None):
            parent = curr
            if curr.data > data:
                curr = curr.left
            else:
                curr = curr.right

        if parent.data > data:
            parent.left = new_node
        else:
            parent.right = new_node

    def find(self, data, node=None):
        if node is None:
            node = self.__root
            print(1)
            if node is None:
                print(2)
                return False
        if node.data == data:
            return True
        elif node.data > data:
            return self.find(node=node.left, data=data)
        else:
            return self.find(node=node.right,data=data)



bst = BinarySearchTree()
bst.insert(1)
bst.insert(1)
bst.insert(1)
bst.insert(1)
bst.insert(1)


from heapq import heappush
#   4       5
# 2   8   3    9
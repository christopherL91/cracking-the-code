#!/usr/bin/env python3

class Node(object):
    """Node class for binary tree"""
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

class Tree(object):
    """Tree class for binary search"""

    def __init__(self, data=None):
        self.root = Node(data)

    def insert(self, data):
        self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def traverseBFS(self, node):
        queue = [node]
        out = [] # output buffer

        while len(queue) > 0:
            currentNode = queue.pop(0)
            out.append(currentNode.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return out

    def inorder(self, node, buf=[]):
        if node is not None:
            self.inorder(node.left, buf)
            buf.append(node.data)
            self.inorder(node.right, buf)

    def preorder(self, node, buf=[]):
        if node is not None:
            buf.append(node.data)
            self.preorder(node.left, buf)
            self.preorder(node.right, buf)

    def postorder(self, node, buf=[]):
        if node is not None:
            self.postorder(node.left, buf)
            self.postorder(node.right, buf)
            buf.append(node.data)

    def test(self):
        d = self.traverseBFS(self.root)
        assert(d == [1,0,5,7,10])

        f = []
        self.inorder(self.root, f)
        assert(f == [0,1,5,7,10])

        j = []
        self.preorder(self.root, j)
        assert(j == [1,0,5,7,10])

        l = []
        self.postorder(self.root, l)
        assert(l == [0,10,7,5,1])

def main():
    tree = Tree(1)
    data = [5,7,10,0]
    for i in data:
        tree.insert(i)
    tree.test()

if __name__ == '__main__':
    main()

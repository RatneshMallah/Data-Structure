class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST(object):
    def __init__(self):
        self.root = None
    
    # O(log(n))
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        
        else:
            self.insertNode(data,self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if not node.leftChild:
                node.leftChild = Node(data)
            else:
                return self.insertNode(data,node.leftChild)
        else:
            if not node.rightChild:
                node.rightChild = Node(data)
            else:
                return self.insertNode(data, node.rightChild)


    def getMinValue(self):
        if self.root:
            return self.get_min(self.root)


    def get_min(self,node):
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data



    def getMaxValue(self):
        if self.root:
            return self.get_max(self.root)


    def get_max(self,node):
        if node.rightChild:
            return self.get_max(node.rightChild)

        return node.data


    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)


    def traverseInOrder(self, node):
        if node.leftChild:
            return self.traverseInOrder(node.leftChild)

        print("%s"%node.data)

        if node.rightChild:
            return self.traverseInOrder(node.rightChild)




bst = BST()
bst.insert(2)
bst.insert(20)
bst.insert(23)
bst.insert(21)
bst.insert(30)
bst.insert(1)

print("min V")
bst.getMinValue()
print("max v")
bst.getMaxValue()
print("traverse")
bst.traverse()

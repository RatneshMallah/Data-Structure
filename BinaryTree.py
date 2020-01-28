class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = None
    
    def insertData(self,data):
        if not self.root:
            self.root = Node(data)
        
        else:
            if data < self.root.data:
                self.insertOnleftChild(data, self.root)
            else:
                self.insertOnrightChild(data, self.root)

    def insertOnleftChild(self,data,node):
        pass
    

    def insertOnrightChild(self,data,node):
        pass


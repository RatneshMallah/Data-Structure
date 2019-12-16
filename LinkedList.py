class Node(object):
	def __init__(self,data):
		self.data = data
		self.nextNode = None 


class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def insert(self,data):
		self.size += 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode


	def remove(self,data):
		if self.head is None:
			return

		self.size -= 1
		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode


	# O(1) 
	def size1(self):
		return self.size

	# O(N)
	# here time complecity is O(N) thats why we should not use this size2
	def size2(self):
		actual_node = self.head
		size = 0
		while actual_node.nextNode is not None:
			actual_node = actual_node.nextNode
			size += 1

		return size


	#O(N)
	def insertEnd(self,data):
		self.size += 1
		newNode = Node(data)
		actual_node = self.head
		while actual_node.nextNode is not None:
			actual_node = actual_node.nextNode

		actual_node.nextNode = newNode


	#O(N)
	def travarseList(self):
		actual_node = self.head
		while actual_node is not None:
			print("%d"%actual_node.data)
			actual_node = actual_node.nextNode

		


test = LinkedList()
test.insert(2)
test.insert(122)
test.insert(3)
test.insertEnd(5)
test.insertEnd(25)

test.travarseList()
print("size : ",test.size1())
print('\n')
test.remove(122)
test.travarseList()
print("size : ",test.size1())
print('\n')
test.remove(25)
test.travarseList()
print("size : ",test.size1())
print('\n')
test.remove(3)
test.travarseList()
print("size : ",test.size1())
print('\n')


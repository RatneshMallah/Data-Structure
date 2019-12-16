# - It is a abstract data type(interface)
# - Basic Operation: pop(), push(), peek()
# - LIFO structure: last in first out
# - A number of programming languages are stack-oriented,
# meaning they define most basic operations(adding two nums, printing a character)
# as taking their arguments from the stack, and placing any return values back on the stack

class Stack:

	def __init__(self):
		self.stack  = []

	def isEmpety(self):
		return len(self.stack) == 0

	def push(self,x):
		self.stack.append(x)

	def pop(self):
		x = self.stack[-1]
		del self.stack[-1]
		return x

	def peak(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)





"""
Applications of stack
---------------------

- Graph algorithms: depth-first search can be implemented with stack(or with recursion)
- Finding Euler-ccycle in a graph
- finding strongly connected component in a graph

"""
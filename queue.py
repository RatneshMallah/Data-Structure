
class Queue:

	def __init__(self):
		self.queue = []

	def queueSize(self):
		return len(self.queue)

	def isEmpety(self):
		return len(self.queue) == 0

	def enqueue(self,x):
		self.queue.append(x)

	def dequeue(self,y):
		z = self.queue[0]
		del self.queue[0]
		return z

	def peek(self):
		return self.queue[0]

	def getQueue(self):
		return self.queue



"""
Queue is FIFO Structured : First in first out.

- It can be Implemented with dynamic arrays as well as with linked list.
- important when iplementing BFS algorithm for graph.

Applications of Queue
---------------------
- When a resource is shared with several consumers (threads) : we store them in a queue
- For Example: CPU sheduling.
- When data is transferred asynchronously (data not necessarily recieved at same rate as sent) between two processes.
- For Example: IO buffers 

"""
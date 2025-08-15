class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Create nodes
one = Node(1)
two = Node(2)
three = Node(3)

# Link nodes
one.next = two
two.next = three
three.next = None

# Head points to the first node
head = one
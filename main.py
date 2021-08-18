import random, math
import alt_function as funcgen

FUNCPOOL_SIZE = 200
funcs = [[funcgen.fg(), funcgen.gen_name(), 1] for i in range(FUNCPOOL_SIZE)]

class Node:
	
	def __init__(self, func, right=None, left=None):
		self.func = func
		self.right = right
		self.left = left
		self.weight = 1
	
	def copy(self, func):
		left = None
		right = None
		
		if self.left is not None:
			left = self.left.copy(self.left.func)
		
		if self.right is not None:
			right = self.right.copy(self.right.func)
		
		return Node(func, right=right, left=left)
	
	def run(self, path):
		#return globals()[self.func](self, cost, prob, reward, path)
		return func_wrapper(self.func[0], self, path)

class Brain:
	
	def __init__(self, root):
		self.root = root
		self.size = 0
	
	def getsize(self, node):
		if not node:
			return
		
		self.size += 1
		self.getsize(node.left)
		self.getsize(node.right)
	
	def get_randnode(self, prob):
		node = self.root
		
		while node is not None:
			child = choose_node(node)
			if not child:
				return node
			if random.random() < prob:
				return child
			else:
				node = child
	
	def think(self, cost, prob, reward, path):
		funcgen.cost = cost
		funcgen.success_prob = prob
		funcgen.reward = reward
		return self.root.run(path)
		
		


# choose from up to two child nodes	
def choose_node(node, weighted=False):
	if not node.right:
		return node.left
	elif not node.left:
		return node.right
	else:
		if not weighted:
			if random.random() < 0.5:
				return node.left
			else:
				return node.right
		else:
			choice = random.choices([node.left, node.right], [node.left.weight, node.right.weight], k=1)[0]
			return choice

# print each function in a tree, starting at the specified node
def traverse(node):
		if not node:
			return
		traverse(node.left)
		traverse(node.right)
		print("{}, weight: {}".format(node.func, node.weight))

def func_wrapper(f, node, path):
	if funcgen.run(f):
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(path)
	else:
		return False

# fitness evaluation
def eval(ind):
	score = 0
	
	# do 50 trial runs
	for i in range(50):
		cost = random.randint(1, 150)
		prob = random.random()
		reward = random.randint(1, 150)
		path = []
		
		# if 'think' returns true, the brain accepted the offer,
		# if false, it declined
		ans = ind.think(cost, prob, reward, path)
		#print(ans)
		
		res = False
		if random.random() < prob:
			res = True
		
		if ans and res:
			score += reward
			for edge in path:
				edge.weight += 1
		if ans and not res:
			score -= cost
			for edge in path:
				edge.weight -= 1
	
	return score

# generate an individual's tree
def gen_tree(size):
	ind = Brain(Node('func'))
	
	node = ind.root
	
	for i in range(size):
		if not node.left:
			f = random.choice(funcs)
			node.left = Node(f)
		elif not node.right:
			f = random.choice(funcs)
			node.right = Node(f)
		node = choose_node(node)
# tree traversal where each node linked to a function in the current results in
# - the counter for that function being incremented
def func_counter(node):
	if not node:
		return
	for f in funcs:
		if funcs[1] == node.func[1]:
			funcs[2] += (node.weight//2)
	func_counter(node.left)
	func_counter(node.right)

def count_funcs(inds):
	for i in inds:
		func_counter(i.root)

# recombination between two parents is performed by randomly selecting one of two parents,
# copying the individual, and then (stochastically) selecting a node as the crossover point,
def recombination(p1, p2):
	root = p1.root.copy('root')
	child = Brain(root)
	
	p1.getsize(p1.root)
	p2.getsize(p2.root)
	
	prob = 1/(p1.size/2)
	
	node = child.root
	
	while node is not None:
#		if not node:
#			break
		if random.random() < prob:
			# select a node from the other parent to copy and insert into the child
			cx_branch = p2.get_randnode(1/(p2.size/2))
			if random.random() < 0.5:
				node.left = cx_branch.copy(cx_branch.func)
				break
			else:
				node.right = cx_branch.copy(cx_branch.func)
				break
		node = choose_node(node)
	
	return child

# I'm thinking that mutation will involve traversing a random path, picking a node with
# probability pm, and randomly choosing a different function to assign to the node
def mutation(ind, pm):
	pass

def gen_ind():
	ind = Brain(Node('root'))
	
	f = random.choice(funcs)
	ind.root.left = Node(f)
	if random.random() < 0.9:
		ind.root.right = Node(random.choice(funcs))
	
	return ind

def gen_pop(size):
	pop = []
	
	for i in range(size):
		pop.append(gen_ind())
	
	return pop

def main(popsize, gens):
	global funcs
	pool = gen_pop(popsize)
	
	for gen in range(gens):
		fitness = []
		nextgen = []
		
		for ind in pool:
			fitness.append(eval(ind))
		
		if gen//50 == 0 and gen > 0 and gen < gens:
#			print("Printing functions")
#			for f in funcs:
#				print(f)
#				print("End of function")
#			print("End of functions")
			nextgen_funcs = []
			for i in range(FUNCPOOL_SIZE):
				selected_inds = random.choices(pool, fitness, k=4)
				count_funcs(selected_inds)
				func_fitness = [f[2] for f in funcs]
				func_parents = random.choices(funcs, func_fitness, k=2)
				child = funcgen.recombination(func_parents[0][0], func_parents[1][0])
				nextgen_funcs.append([child, funcgen.gen_name(), 1])
			
			funcs = nextgen_funcs
		
		for i in range(popsize//2):
			parents = random.choices(pool, fitness, k=2)
			
			c1 = recombination(parents[0], parents[1])
			nextgen.append(c1)
			
			c2 = recombination(parents[1], parents[0])
			nextgen.append(c2)
			
			# I thought this was an interesting route to take for selection, but
			# I decided against it
#			selections = random.choices(pool, k=8)
			
#			scores = {}
			
#			for s in selections:
#				score = eval(s)
#				scores[score] = s
			
#			selections = sorted(scores, reverse=True)
			
#			p1 = scores[selections[0]]
#			p2 = scores[selections[1]]
#			c1 = recombination(scores)
		
		pool = nextgen
	
	fittest = pool[0]
	fit_val = eval(fittest)
	
	for ind in pool[1:]:
		val = eval(ind)
		#print(val)
		if val >= fit_val:
			fittest = ind
			fit_val = val
	
#	print("Printing functions")
#	for f in funcs:
#		print(f)
#		print("End of function")
#	print("End of functions")
				
	return fittest

if __name__ == "__main__":
	ind = main(12, 200)
	print(eval(ind))
	print("Start of traversal:")
	traverse(ind.root)
	print("End of traversal")
	ind.getsize(ind.root)
	print(ind.size)
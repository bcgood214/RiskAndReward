import random, math

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
	
	def run(self, cost, prob, reward, path):
		return globals()[self.func](self, cost, prob, reward, path)

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
		return self.root.run(cost, prob, reward, path)
		
		


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
		print("{}, {}".format(node.func, node.weight))

## beginning of definitions for primitive set

funcs = ['take_over10', 'take_over20', 'take_over50', 'take_over100', 'cost_over10', 'cost_over15', 'cost_over20', 'cost_over25',
 'cost_over30', 'cost_over40', 'cost_over50',
 'prob_over10', 'prob_over15', 'prob_over20', 'prob_over30']

# conns is meant to store which functions can be called by a given function/node
#conns = {}

def root(node, cost, prob, reward, path):
	node = choose_node(node, True)
	if node is None:
		print("Invalid root")
	else:
		return node.run(cost, prob, reward, path)
#conns['root'] = [True for _ in range(len(funcs))]

def take_over10(node, cost, prob, reward, path):
	if reward > 10:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['take_over10'] = [True for _ in range(len(funcs))]

def take_over20(node, cost, prob, reward, path):
	if reward > 20:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['take_over20'] = [True for _ in range(len(funcs))]

def take_over50(node, cost, prob, reward, path):
	if reward > 50:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['take_over50'] = [True for _ in range(len(funcs))]

def take_over100(node, cost, prob, reward, path):
	if reward > 100:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['take_over100'] = [True for _ in range(len(funcs))]

def cost_over10(node, cost, prob, reward, path):
	if cost > 10:
		return False
	else:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over10'] = [True for _ in range(len(funcs))]

def cost_over15(node, cost, prob, reward, path):
	if cost > 15:
		return False
	else:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over15'] = [True for _ in range(len(funcs))]

def cost_over20(node, cost, prob, reward, path):
	if cost > 20:
		return False
	else:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over20'] = [True for _ in range(len(funcs))]

def cost_over25(node, cost, prob, reward, path):
	if cost > 25:
		return False
	else:
		res = choose_node(node, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over25'] = [True for _ in range(len(funcs))]

def cost_over30(children, cost, prob, reward, path):
	if cost > 30:
		return False
	else:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over30'] = [True for _ in range(len(funcs))]

def cost_over40(children, cost, prob, reward, path):
	if cost > 40:
		return False
	else:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over40'] = [True for _ in range(len(funcs))]

def cost_over50(children, cost, prob, reward, path):
	if cost > 50:
		return False
	else:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
#conns['cost_over50'] = [True for _ in range(len(funcs))]

def prob_over10(children, cost, prob, reward, path):
	if prob > 0.1:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['prob_over10'] = [True for _ in range(len(funcs))]

def prob_over15(children, cost, prob, reward, path):
	if prob > 0.15:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['prob_over15'] = [True for _ in range(len(funcs))]

def prob_over20(children, cost, prob, reward, path):
	if prob > 0.20:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['prob_over20'] = [True for _ in range(len(funcs))]

def prob_over30(children, cost, prob, reward, path):
	if prob > 0.30:
		res = choose_node(children, True)
		if res is None:
			return True
		else:
			path.append(res)
			return res.run(cost, prob, reward, path)
	else:
		return False
#conns['prob_over30'] = [True for _ in range(len(funcs))]

## end of definitions for primitive set

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
	pool = gen_pop(popsize)
	
	for gen in range(gens):
		fitness = []
		nextgen = []
		
		for ind in pool:
			fitness.append(eval(ind))
		
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
				
	return fittest

if __name__ == "__main__":
	ind = main(60, 250)
	print(eval(ind))
	traverse(ind.root)
	ind.getsize(ind.root)
	print(ind.size)
# http://codeforces.com/contest/1059/problem/E
class ImpossibleTreeError(Exception):
	pass

# The recursive version was not possible because of the max recusion limit of python

def decompose_in_paths_no_recursive(root_node, weights, tree, max_paths, max_sum):
	sols = {}
	# I simulate recursiveness with a stack
	stack = [root_node]
	while(stack):
		root = stack.pop()
		if(weights[root] > max_sum):
			raise ImpossibleTreeError()
		# If i am a leaf, the solution is easy	
		if len(tree[root]) == 0:
			sols[root] = {"paths": 1, "min_sum":weights[root], "len_min_sum": 1, "len_of_the_shortest": 1,  "sum_of_the_shortest":weights[root]}
		else:
			# Do you have the solution for my children? If not, I need to calculate them before me.
			if not (tree[root][0] in sols):
				stack.append(root)
				for each in tree[root]:
					stack.append(each)
			else:
				# As there are two constraints, I need to track the path that sums the least and the shortest one.
				min_sum = None
				len_of_the_min_sum = None
				len_of_the_shortest = None
				sum_of_the_shortest = None
				paths = 0
				for child in tree[root]:
					each = sols[child]
					del sols[child]
					# Look for the path of minimum sum where this node can be added
					if (each['len_min_sum'] + 1 <= max_paths) and (min_sum is None or (min_sum > each["min_sum"])) :
						min_sum = each["min_sum"]
						len_of_the_min_sum = each["len_min_sum"]
						
					paths += each["paths"]
					# Look for the shortest path where this node can be added
					if (each['sum_of_the_shortest'] + weights[root] <= max_sum) and (len_of_the_shortest is None or (len_of_the_shortest > each["len_of_the_shortest"])):
						len_of_the_shortest = each["len_of_the_shortest"]
						sum_of_the_shortest = each["sum_of_the_shortest"]
						
				# See what happen when I add this node to the minimum sum path
				if not (min_sum is None):
					# Am I able to add it?
					if min_sum + weights[root] <= max_sum:
						min_sum = min_sum + weights[root]
						len_of_the_min_sum += 1
						if len_of_the_min_sum > max_paths:
							min_sum = None
							len_of_the_min_sum = None
					else:
						min_sum = None
						len_of_the_min_sum = None

				# Similar to the previous but for the shortest one
				if not (len_of_the_shortest is None):
					if len_of_the_shortest + 1 <= max_paths:
						len_of_the_shortest = len_of_the_shortest + 1
						sum_of_the_shortest = sum_of_the_shortest +  weights[root]
						if sum_of_the_shortest > max_sum:
							len_of_the_shortest = None
							sum_of_the_shortest = None
					else:
						len_of_the_shortest = None
						sum_of_the_shortest = None
				
				# No candidate path, I need to start a new one
				if min_sum is None and len_of_the_shortest is None:
					sols[root] = {"paths": paths + 1, "min_sum":weights[root], "len_min_sum": 1, "len_of_the_shortest": 1,  "sum_of_the_shortest":weights[root]}
				elif len_of_the_shortest is None and not (min_sum is None):
					# I have to choose the minimum sum path, because I did not want to start a new path
					sols[root] = {"paths": paths , "min_sum":min_sum, "len_min_sum": len_of_the_min_sum, "len_of_the_shortest": len_of_the_min_sum,  "sum_of_the_shortest":min_sum, "paths_shortest":paths_min_sum}
				elif min_sum is None and not (len_of_the_shortest is None):
					# Choose the shortest one to avoid startin a new one
					sols[root] = {"paths": paths, "min_sum":sum_of_the_shortest, "len_min_sum": len_of_the_shortest, "len_of_the_shortest": len_of_the_shortest,  "sum_of_the_shortest":sum_of_the_shortest}
				else:
					# I have two candidate paths for this node
					sols[root] = {"paths": paths, "min_sum":min_sum, "len_min_sum": len_of_the_min_sum, "len_of_the_shortest": len_of_the_shortest,  "sum_of_the_shortest":sum_of_the_shortest}
	return sols[root_node]



def minimum_decomposition(tree, weights, max_paths, max_sum):
	try:
		res = decompose_in_paths_no_recursive(1, weights, tree, max_paths, max_sum)
		return res['paths']
	except ImpossibleTreeError:
		return -1
	

import fileinput
from collections import defaultdict

lines = [line.replace("\n","") for line in fileinput.input()]
n, max_paths, max_sum = map(int, lines[0].split(" "))
weights = {}
i = 1
should_stop = False
for each in lines[1].split(" "):
	weights[i] = int(each)
	if int(each) > max_sum:
		should_stop = True
	i+=1
i = 2
tree = defaultdict(lambda:[])
if len(lines) == 3:
	for each in lines[2].split(" "):
		tree[int(each)].append(i)
		i+=1
if should_stop: 
	print -1
else:
	print minimum_decomposition(tree, weights, max_paths, max_sum)

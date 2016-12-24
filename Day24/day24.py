import itertools
import sys
input = open('puzzleinput', 'r').read().strip().splitlines()

def printField():
	for i in input:
		print ''.join(i)

def getPossible(node):
	x,y = node
	pm = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
	re = []
	for p in pm:
		if input[p[1]][p[0]] != '#':
			re.append(p)
	return re

def bfs(start, end):
	queue = [start]
	visited = [start]
	dist = [0]
	di = 0
	while queue:
		node = queue.pop()
		moves = getPossible(node)
		for m in moves:
			if m not in visited:
				visited.append(m)
				queue.insert(0,m)
				dist.append(dist[di]+1)
				if m == end:
					return dist[di]+1
		di += 1
	return -1

def getCoords(inp):
	re = []
	for i in range(len(input)):
		for j in range(len(input[i])):
			if input[i][j].isdigit() and input[i][j] == inp:
				return (j,i)
	return (0,0)

def getMax():
	max = 0
	for i in range(len(input)):
		for j in range(len(input[i])):
			if input[i][j].isdigit():
				if int(input[i][j]) > max:
					max = int(input[i][j])
	return max

def getDistList(n):
	re = []
	for i in range(n):
		for j in range(i+1,n):
			re.append([(j,i),bfs(getCoords(str(j)), getCoords(str(i)))])
	return re	

def find(state):
	max = getMax()+1
	perm = itertools.permutations(range(1,max))
	li = []
	print 'Search Permutitions...'
	for pe in perm:
		temp = ['0']
		for p in pe:
			temp.append(str(p))
		if state == 1:
			temp.append('0')
		li.append(temp) 
	min = sys.maxint
	minperm = ()
	print 'Getting Distance...'
	dlist = getDistList(max)
	print 'Search shortest...'
	for  l in li:
		st = 0
		print str(li.index(l))+'/'+str(len(li))
		for i in range(len(l)-1):
			for d in dlist:
				if d[0] == (int(l[i]),int(l[i+1])) or d[0] == (int(l[i+1]),int(l[i])):
					st += d[1]
		if st < min:
			min = st
			minperm = l
	print str(li.index(l)+1)+'/'+str(len(li))
	return min

def run():
	a = find(0)
	b = find(1)
	printField()
	print 'Part1: '+str(a)
	print 'Part2: '+str(b)

run()

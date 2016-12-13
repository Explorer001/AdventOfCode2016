fnum = 1364

msize = [45,45]
maze = []
start = [1,1]
fin = [31,39]

elist = [start]
p = [[]]
visited = []
dist = [0]

spath = []

def search():
	di = 0
	visited.append(start)
	while len(elist) > 0:	
		node = elist.pop()
		r = getValidMoves(node[0],node[1])	
		for x in r:
			if x not in visited:
				p.append(node)
				visited.append(x)
				dist.append(dist[di] + 1)	
				elist.insert(0,x)
		di += 1
		if fin in visited:
			break
	return visited	

def backtrack():
	n = fin
	while n != start:
		spath.insert(0,n)
		n = p[visited.index(n)]
	spath.insert(0,start)
	return spath

def markdown(l):
	for x in l:
		a = x[1]
		b = x[0]
		maze[a][b] = 'O '
	maze[fin[1]][fin[0]] = 'x '
	printMaze() 

def getValidMoves(x, y):
	re = []
	possible = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
	for c in possible:
		if c[1] < msize[1] and c[0] < msize[0]: 
			if maze[c[1]][c[0]] == '. ' and c[1] >= 0 and c[0] >= 0:
				re.append(c)
	return re

def initMaze(x,y):
	for i in range(y):
		nx = []
		for j in range(x):
			nx.append('. ')
		maze.append(nx)

def printMaze():
	for y in maze:
		print ''.join(y)

def buildMaze():
	for y in range(len(maze)):
		for x in range(len(maze[y])):	
			maze[y][x] = checkCoord(x, y)

def checkCoord(x, y):
	check = x*x + 3*x + 2*x*y + y + y*y
	check += fnum
	binary = bin(check)
	count = 0
	for b in binary[2:]:
		if b == '1':
			count += 1
	if count%2 == 0:
		return '. '
	else:
		return '# '

initMaze(msize[0], msize[1])
buildMaze()
search()
markdown(backtrack())
print dist[visited.index(fin)]
count = 0
for v in visited:
	if dist[visited.index(v)] <= 50:
		count += 1
print count

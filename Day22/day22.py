input = open('puzzleinput', 'r').read().strip().splitlines()

def createNodeList(input):
	nlist = []
	for i in range(2,len(input)):
		data = input[i].split()
		x = int(data[0].split('-')[1][1:])
		y = int(data[0].split('-')[2][1:])
		size = int(data[1][:-1])
		used = int(data[2][:-1])
		avail = int(data[3][:-1])
		perc = int(data[4][:-1])
		nlist.append((x,y,size,used,avail,perc))
	return nlist

def findPairs(nlist):
	count = 0
	for no in nlist:
		for ni in nlist:
			if no != ni and no[3] <= ni[4] and no[3] != 0:
				count += 1
	return count

def search(start, fin):
	end = fin[3]

def transformToField(nlist):
	f = []
	for i in range(len(nlist)):
		f.append([' ']*31)
	f[0][30] = 'G'
	f[0][0] = '.'
	for n in nlist:
		x,y,s,u,a,p = n
		if f[y][x] == ' ':
			if s < 100 and s > 0:
				f[y][x] = '.'
			if u < 1:
				f[y][x] = '_'
			if s > 100:
				f[y][x] = '#'
	re = []
	for i in range(31):
		re.append(f[i])
	return re

def bfs(start, end):
	queue = [(start[0], start[1])]
	visited = [(start[0], start[1])]
	dist = [0]
	d = 0
	fl = 0
	fin = (end[0], end[1])
	re = ()
	while queue:
		node = queue.pop()
		moves = getPossible(node)
		for m in moves:
			if m not in visited:
				if m == fin:
					if fl == 0:
						re = dist[d] + 1
						fl = 1
					continue
				visited.append(m)
				dist.append(dist[d] + 1)
				queue.insert(0,m)
		if fl == 1:
			break
		d += 1
	return re	

def getPossible(node):
	x,y = node
	re = []
	possible = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
	for p in possible:
		if 0 <= p[0] < len(fd[0]) and 0 <= p[1] < len(fd):
			s,t = p
			if fd[t][s] == '.':
				re.append(p)
	return re

def move():
	start = ()
	end = (29,0)
	for i in range(len(fd)):
		for j in range(len(fd[i])):
			if fd[i][j] == '_':
				start = (j,i)
	steps = bfs(start,end)
	fd[start[1]][start[0]] = '.'
	fd[end[1]][end[0]] = '_'
	while fd[0][0] != 'G':
		x,y = end
		fd[y][x] = 'G'
		fd[y][x+1] = '_'
		if x+2 <= 30:
			fd[y][x+2] = '.'
		end = (x+1,y)
		x,y = end
		steps += 1
		if x-2 >= 0:
			steps += bfs(end,(x-2,y))
			end = (x-2,y)
	return steps

def printField():
	for f in fd:
        	print ''.join(f)

nl = createNodeList(input)
fd = transformToField(nl)
print findPairs(nl)
print move()
printField()

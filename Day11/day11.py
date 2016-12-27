import itertools

testinput = ['1', 'HM@1', 'HG@2', 'LM@1', 'LG@3']
puzzleinput = ['1', 'THG@1', 'THM@1', 'PLG@1', 'PLM@2', 'STG@1', 'STM@2', 'PRG@3', 'PRM@3', 'RUG@3', 'RUM@3']
rng = (1,4)

def getPossible(layer):
	elev = getElevator(layer)
	re = []
	for el in elev:
		upper = [str(int(layer[0])+1)]
		lower = [str(int(layer[0])-1)]
		for i in range(1, len(layer)):
			upper.append(layer[i])
			lower.append(layer[i])
		for e in el:
			for j in range(1, len(layer)):
				if e == layer[j]:
					n = e.split('@')
					upper[j] = n[0]+'@'+str(int(n[1])+1)
					lower[j] = n[0]+'@'+str(int(n[1])-1)
		if rng[0] <= int(upper[0]) <= rng[1]:
			re.append(upper)
		if rng[0] <= int(lower[0]) <= rng[1]:
                        re.append(lower)
	ret = []
	for r in re:
		if valid(r):
			ret.append(r)
	return ret

def valid(layer):
	f = layer[0]
	re = True
	for i in range(1, len(layer)):
		s = layer[i].split('@')
		if s[1] == f and s[0][-1] == 'M':
			safe = 0
			for j in range(1, len(layer)):
				t = layer[j].split('@')
				if t[1] == f and t[0][-1] == 'G':
					if t[0][:-1] == s[0][:-1]:
						safe = 1
					if t[0][:-1] != s[0][:-1] and safe == 0:
						re = False
					else:
						re = True
						
	return re

def getElevator(floor):
	possible = []
	for i in range(1,len(floor)):
		if floor[i].split('@')[1] == floor[0]:
			possible.append(floor[i])
	re = []	
	for p in possible:
		re.append([p])
	for i in range(len(possible)):
		for j in range(i+1, len(possible)):
			a = possible[i].split('@')
			b = possible[j].split('@')
			if (a[0][:-1] == b[0][:-1] or a[0][-1] == b[0][-1]) and a[0] != b[0]:
				re.append([possible[i], possible[j]])
	return re

def getPair(state):
	pair = []
	i = 1
	while i < len(state)-1:
		pair.append((state[i].split('@')[1], state[i+1].split('@')[1]))
		i += 2
	pair.insert(0,state[0])
	return pair

def isIn(conf, ls):
	slist = set(ls)
	perm = itertools.permutations(conf[1:])
	for pe in perm:
		che = [conf[0]]
		for p in pe:
			che.append(p)
		if str(che) in slist:
			return True
	return False

def search(start, end):
	old = 0
	queue = [(start, 0)]
	visited = [str(getPair(start))]
	while queue:
		node, di = queue.pop()
		if di > old:
			print('Depth: '+str(di)+' | Nodes: '+str(len(visited)))
		old = di
		if fin(node,4):
			return (di, len(visited))
		moves = getPossible(node)
		for m in moves:
			pr = getPair(m)
			if not isIn(pr, visited):
				visited.append(str(pr))
				queue.insert(0,(m, di+1))
	return -1
				

def fin(layer, end):
	if str(end) != layer[0]:
		return False
	else:
		for i in range(1, len(layer)):
			c = layer[i].split('@')
			if c[1] != layer[0]:
				return False
	return True

#print isIn(getPair(puzzleinput), 1)
d,n = search(puzzleinput, 4)
print ('Depth: '+str(d)+' | Nodes: '+str(n))

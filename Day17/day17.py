import md5

input = 'veumntbg'

part2 = False

def search():
	nlist = []
	visited = []
	nlist.append([[0,0], input])
	visited.append([[0,0], input])
	p1 = ''
	max = ''
	fl = 0
	while len(nlist) > 0:
		node = nlist.pop()
		pos = getMoves(node)
		for p in pos:
			if p not in visited:
				if p[0] == [3,3]:
					if fl == 0:
						p1 = p[1][len(input):] 
						fl = 1
					else:
						max = len(p[1][len(input):])
					continue
				visited.append(p)
				nlist.insert(0,p)
		if fl == 1 and not part2:
			break
	return (p1, max)

def getMoves(node):
	ha = hash(node[1])
	mov = ['U','D','L','R']
	dir = []
	i = 0
	while i < len(ha):
		if ha[i] != 'a' and not ha[i].isdigit():
			dir.append(mov[i])
		i += 1
	re = []
	for d in dir:
		if d == 'U' and node[0][1]-1 >= 0:
			re.append([[node[0][0], node[0][1]-1],node[1]+d])
		if d == 'D' and node[0][1]+1 < 4:
                        re.append([[node[0][0], node[0][1]+1],node[1]+d])
		if d == 'L' and node[0][0]-1 >= 0:
                        re.append([[node[0][0]-1, node[0][1]],node[1]+d])
		if d == 'R' and node[0][0]+1 < 4:
                        re.append([[node[0][0]+1, node[0][1]],node[1]+d])
	return re 

def hash(s):
	return md5.new(s).hexdigest()[:4]

a,b = search()
print a
part2 = True
a,b = search()
print b

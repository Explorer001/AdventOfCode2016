def getTile(row, pos):
	trap = ['^^.', '.^^', '^..', '..^']
	if row[max(pos-1,0):min(pos+2,len(row))] in trap:
		return '^'
	return '.'

def getRoom(row, size):
	re = []
	r = row
	re.append(r)
	for j in range(size):
		rw = ''
		r = '.' + r + '.'
		for i in range(len(r)):
			rw += getTile(r, i)
		re.append(rw[1:len(rw)-1])
		r = rw[1:len(rw)-1]
	return re

def printRoom(row, size):
	ro = getRoom(row, size-1)
	c = 0
	for r in ro:
		c += r.count('.')
		#print r
	print c

input = '^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^'
printRoom(input, 40)
printRoom(input, 400000)

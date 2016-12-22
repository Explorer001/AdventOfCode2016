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
				

nl = createNodeList(input)
print findPairs(nl)

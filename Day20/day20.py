input = open('puzzleinput', 'r').read().strip().splitlines()

def compareFirst(x, y):
	return int(x.split('-')[0]) - int(y.split('-')[0])

def getValidIP(input):
	fInput = sorted(input, cmp=compareFirst)
	i = 0
	while i < len(fInput)-1:
		if int(fInput[i].split('-')[1])+1 < int(fInput[i+1].split('-')[0]):
			return int(fInput[i].split('-')[1])+1
		i += 1

def part2(input):
	fInput = sorted(input, cmp=compareFirst)
	a = int(fInput[0].split('-')[0])
	b = int(fInput[0].split('-')[1])
	valid = 0
	for f in fInput:
		if int(f.split('-')[0]) > b+1:
			valid += b-a+1
			a = int(f.split('-')[0]) 
			b = int(f.split('-')[1])
		else:
			b = max(b, int(f.split('-')[1]))
	return 2**32 - valid - (b-a+1)

print getValidIP(input)
print part2(input)


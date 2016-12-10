input = open('/home/lukas/AdventOfCode2016/Day10/puzzleinput', 'r').read().strip()

bot = []
ins = []
out = []
cmp = 0

def init():
	max = 0
	split = input.splitlines()
	for s in split:
		parts = s.split()
		if parts[0] == 'bot':
			if int(parts[1]) > max:
				max = int(parts[1])
	for i in range(0, max + 1):
		bot.append([i]) 
		ins.append([])
	for j in split:
		parts = j.split()
		if parts[0] == 'bot':
			ins[int(parts[1])].append(parts[5] + ' ' + parts[6])
			ins[int(parts[1])].append(parts[10] + ' ' + parts[11])

		else:
			bot[int(parts[5])].append(int(parts[1]))

def fin():
	for b in bot:
		if len(b) == 3:
			return False
	return True

def run():
	while not fin():
		for b in bot:
			if len(b) == 3:
				x = b.pop()
				y = b.pop()
				low = min(x, y)
				high = max(x, y)
				if low == 17 and high == 61:
					print str(b[0]) 
				inst = ins[b[0]]
				if inst[0].split()[0] == 'bot':
					bot[int(inst[0].split()[1])].append(low)
				else:
					out.append([int(inst[0].split()[1]), low])
				if inst[1].split()[0] == 'bot':	
					bot[int(inst[1].split()[1])].append(high)
				else:
					out.append([int(inst[1].split()[1]), high])


def printOut():
	c = 1
	for o in out:
		if o[0] == 0 or o[0] == 1 or o[0] == 2:
			c = c * o[1]
	print c

init()
run()
printOut()



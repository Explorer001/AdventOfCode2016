part2 = False

def scramble(input, instruction):
	re = input
	for i in instruction:
		ils = i.split()
		if ils[0] == 'swap':
			if ils[1] == 'position':
				x = int(ils[2])
				y = int(ils[5])
				re = swap(re, x, y)
			elif ils[1] == 'letter':
				x = re.index(ils[2])
				y = re.index(ils[5])
				re = swap(re, x, y)
		elif ils[0] == 'rotate':
			if ils[1] == 'left':
				if part2:
					re = re[-int(ils[2]):]+re[:-int(ils[2])]
				else:
					re = re[int(ils[2]):]+re[:int(ils[2])]
			elif ils[1] == 'right':
				if part2:
					re = re[int(ils[2]):]+re[:int(ils[2])]
				else:
					re = re[-int(ils[2]):]+re[:-int(ils[2])]
			elif ils[1] == 'based':
				if part2:
					re = shiftTest(re, ils[6])
				else:
					rot = re.index(ils[6])
					re = re[-1:]+re[:-1]
					if rot >= 4:
						rot += 1
					for i in range(0,rot):
						re = re[-1:]+re[:-1]
		elif ils[0] == 'reverse':
			x = min(int(ils[2]), int(ils[4]))
			y = max(int(ils[2]), int(ils[4]))
			re = re[:x]+re[x:y+1][::-1]+re[y+1:]
		elif ils[0] == 'move':
			x = int(ils[2])
                        y = int(ils[5])
			li = list(re)
			if part2:
				temp = li.pop(y)
                                li.insert(x,temp)
                                re = ''.join(li)
			else:
				temp = li.pop(x)
				li.insert(y,temp)
				re = ''.join(li)
	return re

def swap(re, x, y):
	s = min(x,y)
	t = max(x,y)
	return re[:s]+re[t]+re[s+1:t]+re[s]+re[t+1:] 

def shiftTest(re, index):
	w = re[1:]+re[:1]
	while based(w, index) != re:
		w = w[1:]+w[:1]
	return w

def based(input, index):
	index = input.index(index)
	re = input[-1:]+input[:-1]
        if index >= 4:
		index += 1   
	for i in range(0,index):
        	re = re[-1:]+re[:-1]
	return re	

inp = open('puzzleinput', 'r').read().strip().splitlines()

print scramble('abcdefgh', inp)
part2 = True
print scramble('fbgdceah', reversed(inp))

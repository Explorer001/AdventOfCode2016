register = [0, 0, 1, 0]
addr = ['a', 'b', 'c', 'd']

data = open('/home/lukas/AdventOfCode2016/Day12/puzzleinput', 'r').read().strip().splitlines()

def run():
	pc = 0
	while pc < len(data):
		inst = data[pc].split()
		if inst[0] == 'inc':
			register[addr.index(inst[1])] += 1
			pc += 1
		if inst[0] == 'dec':
			register[addr.index(inst[1])] -= 1
			pc += 1
		if inst[0] == 'cpy':
			if inst[1].isdigit():
				 register[addr.index(inst[2])] = int(inst[1])
			else:
				 register[addr.index(inst[2])] =  register[addr.index(inst[1])]
			pc += 1
		if inst[0] == 'jnz':
			if inst[1].isdigit():
				if int(inst[1]) != 0:
					pc += int(inst[2])
				else:
					pc += 1	
			else:
				if register[addr.index(inst[1])] == 0:
					pc += 1
				else:
					pc += int(inst[2])

run()

print zip(addr, register)

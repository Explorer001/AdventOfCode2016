register = [0, 0, 0, 0]
addr = ['a', 'b', 'c', 'd']

dat = open('puzzleinput', 'r').read().strip()

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

def run(data):
	pc = 0
	check = []
	while pc < len(data):
		inst = data[pc].split()
		if inst[0] == 'inc':
			register[addr.index(inst[1])] += 1
			pc += 1
		elif inst[0] == 'dec':
			register[addr.index(inst[1])] -= 1
			pc += 1
		elif inst[0] == 'cpy':
			if is_digit(inst[1]) and not is_digit(inst[2]):
				 register[addr.index(inst[2])] = int(inst[1])
			else:
				if not is_digit(inst[2]):
					 register[addr.index(inst[2])] =  register[addr.index(inst[1])]
			pc += 1
		elif inst[0] == 'jnz':
			if inst[1].isdigit():
				if int(inst[1]) != 0:
					if is_digit(inst[2]):
						pc += int(inst[2])
					else:
						pc += register[addr.index(inst[2])]
				else:
					pc += 1	
			else:
				if register[addr.index(inst[1])] == 0:
					pc += 1
				else:
					if is_digit(inst[2]):
                                                pc += int(inst[2])
                                        else:
                                                pc += register[addr.index(inst[2])]
		elif inst[0] == 'tgl':
			chg = pc + register[addr.index(inst[1])]
			if chg < len(data):
				cdata = data[chg].split()
				if len(cdata) == 2:
					if cdata[0] == 'inc':
						data[chg] = 'dec '+cdata[1]
					else:
						data[chg] = 'inc '+cdata[1]
				elif len(cdata) > 2:
					if cdata[0] == 'jnz':
						data[chg] = 'cpy '+cdata[1]+' '+cdata[2]
					else:
						data[chg] = 'jnz '+cdata[1]+' '+cdata[2]
			pc += 1
		elif inst[0] == 'mul':
			register[addr.index(inst[3])] =  register[addr.index(inst[1])]* register[addr.index(inst[2])]
			pc += 1	
		if inst[0] == 'out':
			if is_digit(inst[1]):
				check.append(int(inst[1]))
			else:
				check.append(register[addr.index(inst[1])])
			pc += 1	
		if len(check) > 128:
			return check

def bruteforce():
	fin = False
	test = 0
	print 'Testing...'
	while not fin:
		register[0] = test
		print test
		check = run(dat.splitlines())
		fin = True
		for i in range(len(check)-1):
			if check[i] == check[i+1]:
				fin = False
		test += 1

bruteforce()

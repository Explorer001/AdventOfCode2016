import time

disp = [["."]*50,["."]*50,["."]*50,["."]*50,["."]*50,["."]*50] 

with open('/home/lukas/AdventOfCode2016/Day8/puzzleinput', 'r') as ins:
	instr = ins.read()

instri = instr.splitlines()

def rotate(l, n):
    return l[-n:] + l[:-n]

def updateScreen(inst):
	inlist = inst.split()
	if inlist[0] == "rect":
		dats = inlist[1].split("x")	
		x = int(dats[0])
		y = int(dats[1])
		for i in range(0, y):
			for j in range(0,x):
				disp[i][j] = "#"
	if inlist[0] == "rotate":
		if inlist[1] == "row":
			disp[int(inlist[2][2:])] = rotate(disp[int(inlist[2][2:])], int(inlist[4]))
		if inlist[1] == "column":
			f = int(inlist[2][2:])
			col = disp[0][f] + disp[1][f] +disp[2][f] +disp[3][f] +disp[4][f] +disp[5][f]
			ne = rotate(col, int(inlist[4]))
			for cn in range(0, len(disp)):
				disp[cn][f] = ne[cn]


def getActivePixels(li):
	count = 0
	for i in range(0, len(disp)):
		for j in range(0, len(disp[i])):
			if disp[i][j] == "#":
				count += 1
	return count	


for s in instri[:-1]:
	updateScreen(s)

for d in disp:
	print "".join(d)

print(getActivePixels(disp))


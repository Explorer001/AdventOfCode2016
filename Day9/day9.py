with open('/home/lukas/AdventOfCode2016/Day9/puzzleinput', 'r') as puin:
	p = puin.read().strip()

def decompress(string):
	dec = ''
	marker = ''
	#print string
	i = 0
	while i < len(string):
		if string[i] != '(':
			dec += string[i]
			i += 1
		else:
			marker = getMarker(i+1, string[i+1:])
			i = int(marker[2]) + int(marker[0])
			for j in range(0, int(marker[1])):
				dec += string[int(marker[2]):int(marker[2])+int(marker[0])]
	return dec

def getMarker(i, s):
	marker = ''
	for j in range(0,len(s)):
		if s[j] == ')':
			break
		else:
			marker += s[j]
	mlist = marker.split('x')
	nindex = str(i + j + 1)
	mlist.append(nindex)
	return mlist	

print(len(decompress(p)))

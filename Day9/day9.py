with open('/home/lukas/AdventOfCode2016/Day9/puzzleinput', 'r') as puin:
	p = puin.read().strip()

def decompress(string):
	dec = ''
	marker = ''
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

def recDec(string):
	l = 0
	if '(' not in string:
		return len(string)
	while '(' in string:
		l += string.find('(')
		string = string[string.find('('):]
		marker = string[1:string.find(')')].split('x')
		string = string[string.find(')') + 1:]
		l += recDec(string[:int(marker[0])]) * int(marker[1])		
		string = string[int(marker[0]):]
	l += len(string)
	return l	

print(len(decompress(p)))
print(recDec(p))

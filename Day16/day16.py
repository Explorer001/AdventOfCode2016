l = 35651584
d = '10001110011110000'

def generateData(input):
	if len(input) >= l:
		return input[:l]
	else:	
		return generateData(input + '0' + flip(input)[::-1])

def getCsum(input):
	csum = ''
	i = 0
	while i < len(input) - 1:
		if input[i] == input[i+1]:
			csum += '1'
		else:
			csum += '0'
		i += 2
	if len(csum)%2 == 0:
		return getCsum(csum)
	return csum	

def flip(string):
	re = ''
	for s in string:
		if s == '1':
			re += '0'
		else:
			re += '1'
	return re

a = generateData(d)
print a, getCsum(a)

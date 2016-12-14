import md5

part2 = False

p2h = []

def generateP2Hash(input):
	print 'generating'
	for i in range(50000):
		print i
		h = hash(input+str(i))
		for j in range(2016):
			h = hash(h)
		p2h.append(h)
	print 'fin'

def hash(s):
	return md5.new(s).hexdigest()

def containsTriple(hash):
	for i in range(len(hash)-2):
		if same(hash[i:i+3]):
			return ['T', hash[i]]
	return ['F']

def same(s):
	for i in range(1,len(s)):
		if s[0] != s[i]:
			return False
	return True

def containsFive(h):
	for i in range(len(h)-4):
		if same(h[i:i+5]):
			return ['T', h[i]]
	return ['F']

def isKey(h, index, symbol):
	end = index + 1000
	index += 1
	for i in range(index,end):
		check = hash(h+str(index))
		c = containsFive(check)
		if c[0] == 'T':
			if c[1] == symbol:
				return True
		index += 1
	return False	

def findKey(input):
	keys = []
	count = 0
	index = 0
	while count < 64:
		print keys
		h = hash(input+str(index))
		t = containsTriple(h)
		if t[0] == 'T':
			if isKey(input, index, t[1]):
				keys.append(index)
				count += 1
		index += 1
	print keys

def isKey2(index, symbol):
	end = index + 1000
	index += 1
	part = p2h[index:end]
	for p in part:
		c = containsFive(p)
		if c[0] == 'T':
			if c[1] == symbol:
				return True
	return False

def findKey2(input):
	generateP2Hash(input)
	keys = []
	i = 0
	while len(keys) < 64:
		print keys
		h = p2h[i]
		t = containsTriple(h)
		if t[0] == 'T':
			if isKey2(i, t[1]):
				keys.append(i)
		i += 1
	print keys

#findKey('jlmsuwbz')
findKey2('jlmsuwbz')


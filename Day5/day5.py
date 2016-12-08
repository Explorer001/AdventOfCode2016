import md5

def hashString(s):
	return md5.new(s).hexdigest()

def getPW(s):
	pw = ""
	count = 0
	while len(pw) < 8:
		con = s + str(count)
		hash = hashString(con)
		if hash[:5] == "00000":
			pw += str(hash[5:6])
			print(pw)
		count += 1
	return pw

def getPWbyIndex(s):
	pw = ["_","_","_","_","_","_","_","_"]	
	count = 0
	while "_" in pw:
		con = s + str(count)
		hash = hashString(con)
		if hash[:5] == "00000":
			if hash[5:6].isdigit():
				if int(hash[5:6]) < 8:
					if pw[int(hash[5:6])] == "_":
						pw[int(hash[5:6])] = hash[6:7]
						print("".join(pw))		
		count += 1
	return "".join(pw)

print(getPW("ugkcyxxp"))
print(getPWbyIndex("ugkcyxxp"))

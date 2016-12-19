def solve(input):
	index = 0
	while 2**index < input:
		index += 1
	index -= 1
	winner = 1
	for i in range(2**index,2**(index+1)):
		winner += 2
		if i == input:
			break
	winner -= 2	
	return winner

print solve(3005290)

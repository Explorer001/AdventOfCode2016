disk = [[17,1],[7,0],[19,2],[5,0],[3,0],[13,5],[11,0]]

def run():
	time = 0
	conf = disk[:]
	while not fin(conf):
		conf = []
		stime = time + 1
		for d in disk:
			conf.append((d[1] + stime)% d[0])
			stime += 1
		print conf
		if not fin(conf):
			 time += 1
	print time


def fin(input):
	flag = 0
	for d in input:	
		if d != 0:
			flag = 1
	if flag == 0:
		return True
	return False

run()

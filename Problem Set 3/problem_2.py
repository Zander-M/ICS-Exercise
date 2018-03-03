# World Series Champions
with open('WorldSeriesWinners.txt') as f:
	ls = f.readlines()
	name = input()
	count = 0
	for i in ls:
		if name in i:
			count += 1
	print(count)
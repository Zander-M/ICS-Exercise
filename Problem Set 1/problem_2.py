# prime number in 100
ls = []
for i in range(2, 100):
		ls.append(i)
k = 0
while k ** 2 <= 100:
	for j in range(len(ls)):
		if ls[k] != 0 and ls[j] != ls[k] and ls[j] % ls[k] == 0:
			ls[j] = 0
	k += 1
ls = filter(lambda x: x != 0, ls)
for l in ls:
	print(l)

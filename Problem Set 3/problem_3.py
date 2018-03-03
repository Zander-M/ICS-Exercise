# Caesar Encoding
ls1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
ls2 = []
ls3 = []
sen = input()
for j in sen:
	if j.isupper():
		ls2.append(1)
	else:
		ls2.append(0)
	for i in range(26):
		ls3.append(ls1.find(j)-i)
	print(ls3)

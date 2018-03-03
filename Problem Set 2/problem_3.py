def capitalize(st):
	w = st[0]
	for i in st[1:]:
		if i.isupper():
			w += " " + i.lower()
		else:
			w += i
	return w


print(capitalize(input()))
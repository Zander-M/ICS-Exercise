def reverse_vowel(st):
	v = set('aeiou')
	ls = [i for i in st if i in v]
	w = ''
	for j in st:
		if j in v:
			w += ls.pop()
		else:
			w += j

	return w


print(reverse_vowel(input()))
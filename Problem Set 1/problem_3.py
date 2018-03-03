d = dict
d[0] = 'green'
for i in range(1, 37):
	if i <= 10 and i % 2 == 0 or 19 <= i <= 28 and i % 2 == 0 or 10 <= i <= 18 and i % 2 == 1 or i >= 29 and i % 2 ==1:
		d[i] = 'black'
	else:
		d[i] = "red"
num = int(input())
if num <= 36:
	print(d[num])
else:
	print("out of range")


def roman(num):
	result = ''
	ls = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], \
		['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC','DCCC', 'CM'], ['', 'M', 'MM', 'MMM']]
	if num >= 1000:
		result += ls[3][(num // 1000)]
	if num >= 100:
		result += ls[2][((num % 1000) // 100)]
	if num >= 10:
		result += ls[1][((num % 100) // 10)]
	result += ls[0][(num % 10)]
	return result


print(roman(int(input())))



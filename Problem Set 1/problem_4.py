num = int(input())
if num < 60:
	print(num,'sec')
elif num< 3600:
	print(num / 60, 'min')
elif num < 86400:
	print(num / 3600, 'hr')
else:
	print(num / 86400, 'day')
# Name Search
boy = open('BoyNames.txt')
girl = open('GirlNames.txt')
lsB = boy.read().splitlines()
lsG = girl.read().splitlines()
Bname = input("Boy's name: ")
Gname = input("Girl's name: ")
if Bname in lsB:
	print("Boy's name is in the list")
if Gname in lsG:
	print("Girl's name is in the list")
boy.close()
girl.close()
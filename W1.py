# E1
# price = int(input("please input the price of the food "))
# print("this is the price for your meal: {}".format(price*(1+0.15+0.07))) #15% of tip and 7% of tax 113
# E2
# people = int(input("please give the number of the people attending the cookout:"))
# num = int(input("Please give the number of hotdogs each people will be given:"))
# num_of_hot_dog = people * num
# if num_of_hot_dog % 8 == 0:
# 	pack_of_bread = num_of_hot_dog // 8
# else:
# 	pack_of_bread = num_of_hot_dog // 8 +1
# if num_of_hot_dog % 10 ==0:
# 	pack_of_hot_dog = num_of_hot_dog // 10
# else:
# 	pack_of_hot_dog = num_of_hot_dog //10 +1
# print(pack_of_hot_dog,pack_of_bread,pack_of_hot_dog * 10 - num_of_hot_dog,pack_of_bread * 8 - num_of_hot_dog)
# E3
# quantity = int(input("please input the number of the software"))
# price = 99
# if quantity < 10:
# 	dis = 1
# elif quantity <= 19:
# 	dis = 0.9
# elif quantity <= 49:
# 	dis = 0.8
# elif quantity <= 99:
# 	dis = 0.7
# else:
# 	dis = 0.6
# discount = price * quantity * (1 - dis)
# amount = price * quantity * dis
# print(discount,amount)
#Prime Number
#  num = 0
# while 1:
# 	num = int(input("please input a positive number"))
# 	if num < 0:
# 		break
# 	elif num == 1:
# 		print("is not prime")
# 	elif num == 2:
# 		print("is prime")
# 	else:
# 		for i in range(2,num):
#
# 			if num % i ==0:
# 				print("is not prime")
# 				break
# 			else:
# 				print("is prime")



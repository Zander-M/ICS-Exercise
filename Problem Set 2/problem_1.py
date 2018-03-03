def length_of_last_word(st):
	ls = st.split(" ")
	if ls[-1].isalpha():
		return len(ls[-1])
	else:
		return 0


length_of_last_word(input())
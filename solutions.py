def max_int(a):
	'''
	The function returns the largest integer
	in a given list a
	'''
	max_num = 0
	for num in a:
		if num > max_num:
			max_num = num
	return max_num	
		
def half_reverse(s):
	'''
	Given a string s, the function reverses the second
	half of the string
	'''
	rev_string = ""
	first_half = ""
	string_length = len(s)
	halfs = string_length // 2
	if string_length%2 == 0:
		rev_string = s[string_length:halfs-1:-1]
		first_half = s[0:halfs]
	else:
		rev_string = s[string_length:halfs:-1]
		first_half = s[0:halfs+1]
	return first_half + rev_string

def list_power(a):
	'''
	The function raises every integer in the list to the 
	power of it's index. e.g. a = [2,4,3] returns [0,1,8]
	'''
	new_set = []
	for number in a:
		ind_num = a.index(number)
		new_set.append(number**ind_num)
	return new_set


def max_int(a):
	'''
	The function returns the largest integer
	in a given list a
	'''
	pass


def half_reverse(s):
	'''
	Given a string s, the function reverses the second
	half of the string
	'''
	pass

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


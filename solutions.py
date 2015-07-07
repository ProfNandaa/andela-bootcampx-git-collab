def max_int(a):
	'''
	The function returns the largest integer
	in a given list a
	'''
	maxs=0
	for value in a: 
		if maxs > value:
			maxs = value
	return maxs
	
def half_reverse(s):
	'''
	Given a string s, the function reverses the second
	half of the string
	'''
	c = len(s)
	d = c / 2
	if c%2 == 0:
		return s[c:d-1:-1]
	else:
		return s[c:d:-1]

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


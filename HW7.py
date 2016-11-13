#Andrew Tuttle
#GTID: 903110416
#Section A3
#I have not recived or given aid on this assignment, and used only this semester's course materials.
def square_contents(alist): 
	if len(alist) == 1:
		alist[0] = alist[0] ** 2
		return alist
	else:
		alist[-1] = alist[-1] ** 2
		new_value = square_contents(alist[:-1])
	return new_value + [alist[-1]]
	
def factorial_dictionary(an_Int):
	aDict = {}
	if an_Int == 1:
		aDict[an_Int] = 1
		return aDict
	else:
		aDict[an_Int] = an_Int * factorial_dictionary(an_Int - 1)[an_Int - 1]
		return {**aDict, **(factorial_dictionary(an_Int - 1))}

def solve_eq(mathEq):
	operatorList = ['*','/','+','-']
	i = 0
	newString = ""
	if type(mathEq) == str:
		for each in mathEq:
			newString = newString + " "
			newString = newString + each
			newString = newString + " "
		mathEq = newString
		mathEq = mathEq.split()
		for each in mathEq:
			if (each not in operatorList) == True:
				try: 
					mathEq[i] = int(each)
				except:
					mathEq[i] = float(each)
			i += 1
	if len(mathEq) == 1:
		return(mathEq[0])
	else:
		if '*'in mathEq or '/' in mathEq:
			multi = len(mathEq)
			divide = len(mathEq)
			if '*' in mathEq:
				multi = mathEq.index('*')
			if '/' in mathEq:
				divide = mathEq.index('/')
			center = min(multi,divide)
			if center == multi:
				mathEq[center] = ((mathEq[center - 1]) * (mathEq[center + 1]))
			elif center == divide:
				mathEq[center] = ((mathEq[center - 1]) / (mathEq[center + 1]))
			del mathEq[center - 1]
			del mathEq[center]
		else:
			add = len(mathEq)
			subtract = len(mathEq)
			if '+' in mathEq:
				add = mathEq.index('+')
			if '-' in mathEq:
				subtract = mathEq.index('-')
			center = min(add,subtract)
			if center == add:
				mathEq[center] = ((mathEq[center - 1]) + (mathEq[center + 1]))
			elif center == subtract:
				mathEq[center] = ((mathEq[center - 1]) + (mathEq[center + 1]))
			del mathEq[center - 1]
			del mathEq[center]
		solve_eq(mathEq)
		return mathEq
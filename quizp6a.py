def flatten(aList):
	
	new = []
	for x in aList:
		if type(x) is list or type(x) is tuple:
			for v in x:
				new = aList + v
			else:
				new.append(x)
	return new			
	
flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]]])	
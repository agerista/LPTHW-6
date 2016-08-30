def flatten(aList):

	if isinstance(aList, list):
		return aList
	else:
		holder = []
		for sub in aList:
			holder.append(flatten(sub))
		return holder		


def flatten(aList):
	
	new = []
	for x in aList:
		if type(x) is list or type(x) is tuple:
			for v in x:
				new.append(x)
		else:
			new.append(x)
	return new				





def flatten(aList):

	if not isinstance(aList,list):
        return aList
    else:
        holder = []
        for sub_content in aList:
            holder.append(flatten(sub_content))
        return holder


"""
def flatten(aList):

	flat = []

	for x in aList:
		if isinstance(x, list):
			newlist = x
			newlist = newlist[1:]
		
		else:
			flat.append(x)	



def flatten(aList):

	flat = []
	
	for x in aList:
		for y in x:
			
			if y is list:
			    for a in y:
			        for b in a:
			            flat.append(b)
			            print flat
			if y is not list:
			    
			    flat.append(y)
			    print flat
			
	return flat		


def flatten(aList):

	flat = []
	
	for i in aList:
		if type(i) is list:
			
			flat.extend(i)
		else:
			flat.append(i)	
			
	return flat		



def flatten(aList):

	flat = []
	
	for x in aList:
		for y in x:
			
			flat.append(y)
			
	return flat		

def flatten(aList):

	aListFlat = aList[:]
	flat = []
	x = 1

	if aListFlat == []:
		return []
		
	else:
		for e in aListFlat:
			flat = aListFlat[1:][1:]	
		
	return x + flat

def flatten(aList):

	aListFlat = aList[:]
	flat = []

	for e in aListFlat:
		
		
		aListFlat[1:]
		flat.append(e)
		print flat
		
	return flat	

	
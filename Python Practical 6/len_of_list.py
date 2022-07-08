# 1. Program to find length of list using recurrsion

def length(b):
	if not b:
		return 0	
	return 1 + length(b[1::2])+length(b[2::2])
a=[1,2,3,5,6,78,9]
print("Length of list is: ",length(a))

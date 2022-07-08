# 4. program to find intersection of two list

def intersection(list1,list2):
	list3=[value for value in list1 if value in list2]
	return list3
list1=[]
a=int(input("Enter the length of the list ="))
print("Enter the list:")
for i in range(a):
	b=int(input())
	list1.append(b)
list2=[]
c=int(input("Enter the length of the list ="))
print("Enter the list:")
for i in range(c):
	d=int(input())
	list2.append(d)
print("Intersection of two list is:",intersection(list1,list2))

# 2. Program to remove ith occurence of given word in a list where words repeat

a=(input("Enter String:").split(" "))
N=len(a)
c=0
lis=[]
print(a)
w=input("Enter word to remove:")
n=int(input("Enter occurance of word"))
for i in a:
	if i==w:
		c+=1
		if c!=n:
			pass
	else:
		lis.append(i)
if c==0:
	print("Item not found")
else:
	print(lis)
print()

# Program to sort dictionry using key and value

dic={1:"python",3:"cpp",4:"java",2:"javascript"}
print("Sort according to keys:")
for i in sorted (dic):
	print((i,dic[i]),end=" ")
print("sort acording to vlues:")
print(sorted(dic.items(),key=lambda x:(x[1],x[0])))

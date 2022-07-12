# Program to take two list as input and convert them into dictionary and print dictionary

l1=[15,30,45,60,90]
l2=["a","b","m","p","o"]
dic={l1[i]:l2[i] for i in range(len(l1))}
print(dic)

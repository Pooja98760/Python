# 2. program to extract elements with frequency greater than k

list1 = [5, 6, 5, 7, 7, 5, 7, 7, 8, 8]
  
print("The original list : " + str(list1))
  
K = 2
  
res = [] 
for i in list1:     
    freq = list1.count(i)  
    if freq > K and i not in res: 
        res.append(i)
   
print("The required elements : " + str(res))

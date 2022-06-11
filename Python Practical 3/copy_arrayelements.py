# copy all elements of one array into other

arr1 = [11, 12, 30, 45, 15]     
        
arr2 = [None] * len(arr1)    
         
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i]     
        
print("Elements of original array: ")    
for i in range(0, len(arr1)):    
   print(arr1[i])    
     
print()    
     
#Displaying elements of array arr2     
print("Elements of new array: ")    
for i in range(0, len(arr2)):    
   print(arr2[i]) 

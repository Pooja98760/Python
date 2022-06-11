# Print elements of array in reverse order

arr = [7,8,9,10,11,12]     
print("Original array: ")    
for i in range(0, len(arr)):    
    print(arr[i])     
print("Array in reverse order: ")    
    
for i in range(len(arr)-1, -1, -1):     
    print(arr[i]) 

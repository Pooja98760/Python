# Sort the elements of array in ascending and descending order

n=int(input("Enter size of array: "))
arr=list(map(int,input("Enter elements of array: ").split()))
arr.sort(reverse=False) 
print("Ascending order array: ")
print(arr)
arr.sort(reverse=True)
print("Descending order array: ")
print(arr)

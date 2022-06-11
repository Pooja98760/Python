# Print largest and smallest elements in array

arr = [10, 89, 9, 56, 4, 80, 8]
smallest = arr[0]
largest = arr[0]

for i in range(len(arr)):
  if arr[i] < smallest:
    smallest = arr[i]
  if arr[i] > largest:
    largest = arr[i]

print (smallest)
print (largest)

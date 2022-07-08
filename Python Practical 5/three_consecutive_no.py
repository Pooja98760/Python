# Program to check if the list contain three consecutive numbers

a = [2,2,2,56,23,29,29,29,64]
size = len(a)

for i in range(size-2):
    if a[i] == a[i+1] and a[i+1] == a[i+2]:
        print(a[i])

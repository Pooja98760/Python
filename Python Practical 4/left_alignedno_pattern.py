# 6. Python program to print left aligned number pattern

row = int(input("Enter the no of rows: "))
for i in range(row):
    for j in range(row-i-1):
        print(" ",end = " ")
    for j in range(i+1):
        print(j+1,end = " ")
    print()

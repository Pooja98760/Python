# 5. Python program to print diamond pattern

row = int(input("Enter the no of rows: "))
for i in range(0,row):
    print(" " * (row-i) + " *" * (i+1))
for j in range(row-1):
    print(" " * (j+2) + " *" * (row-1-j))

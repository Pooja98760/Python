# 1. Program to print perfect no

n = int(input("Enter any number: "))
sum = 0
for i in range(1,n):
    if(n%i == 0):
        sum = sum+i
if(sum == n):
    print("The given number is a perfect no")
else:
    print("The given number is not a perfect no")

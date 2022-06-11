# Program to print pronic no between 1 to 100

def isPronicNumber(num):  
    flag = False  
      
    for j in range(1, num+1):    
        if((j*(j+1)) == num):  
            flag = True  
            break  
    return flag  
   
#Displays pronic numbers between 1 and 100  
print("Pronic numbers between 1 and 100: ") 
for i in range(1, 101):  
    if(isPronicNumber(i)):  
        print(i) 
        print(" ")  

# Q2.A Write a python program to perform operations on complex numbers creating class complex_number


class Complex():
    def _init_(self,a=0,b=0):
        self.a = a
        self.b = b
    def _str_(self):
        return "{0}+{1}j".format(self.a,self.b)

    def _add_(self,other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a,b)
    
    def _sub_(self,other):
        a = self.a - other.a
        b = self.b - other.b
        return Complex(a,b)
    
    def _mul_(self,other):
        return Complex(a*b)
    
    def _ge_(self,other):
        self_ge = (self.a ** 2)+(self.b **2)
        other_ge =(other.a ** 2)+(other.b **2)
        return self_ge>=other_ge

a=complex(input("Enter First Complex Number: "))
b=complex(input("Enter Second Complex Number: "))
real1,img1 = ((str(a).strip('(')).strip(')')).strip('j').split('+')
real2,img2 = ((str(b).strip('(')).strip(')')).strip('j').split('+')
print("--------------------------------------------------")
c1= Complex(int(real1),int(img1))
c2 = Complex(int(real2),int(img2))
print("--------------------------------------------------")
print("Additon Of 2 complex number---> ",c1+c2)
print("Subtraction of 2 complex number---> ",c1-c2)
print("Multiplication of 2 complex number---> ",str(c1*c2).strip('+0j'))
print("C1>=C2: ",c1>=c2)
print("C1==C2: ",c1==c2)

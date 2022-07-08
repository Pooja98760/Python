# Program to compute difference between two list

def Diff(li1,li2):
    li_dif = [i for i in li1+li2 if i not in li1 or i not in li2]
    return li_dif
li1 = [15,30,45,60,90]
li2 = [15,45,90]
print(Diff(li1,li2))

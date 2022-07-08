# 1. Program to count unique value inside the list


input_list = [1, 4, 2, 5, 8, 4, 4, 8,1,7]
list1 = []
count = 0

for item in input_list:
    if item not in list1:
        count += 1
        list1.append(item)
 
# printing the output
print("No of unique items are:", count)

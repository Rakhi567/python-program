list1=[]
list2=[]
sum1=0
sum2=0
len1=int(input("how many numbers do you want to add in the first list"))
for i in range(0,len1):
    inp=int(input("enter the value of elements"))
    list1.append(inp)
len2=int(input("how many numbers do you want to add in the second list"))
for i in range(0,len2):
    inp=int(input("enter the value of elements"))
    list2.append(inp)
if(len(list1)==len(list2)):
    print("two list are of same length")
else:
    print("list have diff length")
for num in list1:
     sum1+=num
for num in list2:
    sum2+=num
if sum1==sum2:
    print("the sum of values of elements in both lists are equal")
else:
    print("the sum of values of both lists elements are different")
for num in list1:
    if num in list2:
        print(num,"found in both list\n")

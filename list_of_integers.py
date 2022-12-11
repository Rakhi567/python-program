lis=[]
a=[]
n=int(input("Enter the limit of the list \t"))
print("Enter the list of elements")
for i in range(0,n):
 print("Enter the element no:-{}:".format(i+1))
 elm=int(input())
 lis.append(elm)
print("The entered list is ",lis)
for i in lis:
 if i>100:
     a.append(i)
 else:
     print("Over")
print("The values greater than 100 ", a)
l=[]
even=[]
n=int(input("Enter the limit of list "))
print("Enter the integers into the list ")
for i in range(0,n):
 print("Enter the element no: -{}".format(i+1))
 elm=int(input())
 l.append(elm)
print("List of integers are ",l)
for i in l:
 if i%2!=0:
  even.append(i)
print("List of integers removing even numbers are ",even)

list1=[]
len=int(input("Enter the number of names you want to insert "))
for i in range(0,len):
 print("Enter the name ",i+1," you want to insert ")
 fname=input()
 list1.append(fname)
 count_a=0
for names in list1:
 count_a+=names.count("a")
print("Occurrence of a in given list is",count_a)

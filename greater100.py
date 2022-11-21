len=int(input("how many numbers do you want to store?"))
inputvaluelist=[]
for num in range(0,len):
    inputvalue=int(input("enter a value"))
    if inputvalue>100:
        inputvaluelist.append("over")
    else:
        inputvaluelist.append(inputvalue)
print(inputvaluelist)

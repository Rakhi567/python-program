def length(flist,slist):
 print("a.Length of list 1\t",len(flist))
 print("\tLength of list 2\t",len(slist))
 if len(flist)==len(slist):
  print("\tBoth list have same size")
 else:
  print("Different length ")
def sumoflist(flist,slist):
 s1=0
 s2=0
 for num in flist:
  s1+=num
 for num in slist:
  s2+=num
  if s1==s2:
    print("b.Sum are same ", s1, " ,", s2)
 else:
    print("b.Sum are different for both list ", s1, " ,", s2)


def findele(flist, slist):
    for num in flist:
        if num in slist:
         print("c.", num, " found in both list\n")
flist = []
slist = []
len1 = int(input("Enter the number of elements you want to add on list 1 "))
for i in range(0, len1):
    print("Enter the element ", i + 1)
    inp = int(input())
    flist.append(inp)
len2 = int(input("Enter the number of elements you want to add on list 2 "))
for i in range(0, len2):
    print("Enter the element ", i + 1)
    inp = int(input())
    slist.append(inp)
length(flist, slist)
sumoflist(flist, slist)
findele(flist, slist)

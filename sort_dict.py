d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
l=list(d.items())
 #convert the given dict. into list
l.sort() #sort the list
print('Ascending order is  ',l)
l=list(d.items())
l.sort(reverse=True) #sort in reverse order
print('Descending order is ',l)
dict=dict(l) # convert the list in dictionary
print("Dictionary ",dict)
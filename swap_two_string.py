def charswap(a, b):
 new_a = b[:1] + a[1:]
 new_b = a[:1] + b[1:]
 return new_a + ' ' + new_b
a=input("Enter string 1 ")
b=input("Enter string 2 ")
print("Swapped strings\n")
print(charswap(a,b))

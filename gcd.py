def compute_gcd(x, y):
    if x > y:
        s = y

    else:
        s = x

    for i in range(1, s + 1):
        if ((x % i == 0) and (y % i == 0)):
             gcd = i
    print("G.C.D is ", gcd)


a = int(input("Enter the a value to find GCD "))
b = int(input("Enter the another value to find GCD "))
compute_gcd(a, b)

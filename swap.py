def swap(str1):
    # storing the first character
    start = str1[0]

    # storing the last character
    end = str1[-1]

    swapped_string = end + str1[2:-1] + start
    print(swapped_string)


a = input("Enter the string ")
swap(a)

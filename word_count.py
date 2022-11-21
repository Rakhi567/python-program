text = input("Enter the text to count its words \n")
word_count = {}
word_lst = text.split(" ")
for i in word_lst:
    count = 1
    if i not in word_count.keys():
        word_count.update({i: count})
    else:
        count = word_count.get(i)
        count = count + 1
        word_count.update({i: count})


for i in word_count.keys():
    print(f"{i} = {word_count.get(i)}")


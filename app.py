introduction = input("Enter yout introduction")
charectercount = 0
wordcount = 1
for i in introduction:
    charectercount = charectercount+1
    if(i == " "):
        wordcount = wordcount+1
print("number of charecter is ")
print(charectercount)
print("number of words in the introduction is ")
print(wordcount)
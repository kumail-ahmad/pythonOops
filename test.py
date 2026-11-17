# import string
# import random 
# name = input("Enter name : ").lower().replace(" ","")
# print(name)

# listName=list(name)
# random.shuffle(listName)
# anagram=" ".join(listName)
# print(anagram)

temp=list(map(int,input().split()))
total =0
for i in temp:
    total=total+i//32
print(total)
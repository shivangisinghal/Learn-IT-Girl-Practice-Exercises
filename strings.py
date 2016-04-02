string1= input("Enter a string in capital letters:")
string2= input("Enter another string:")
a=0
b=0
for i in range(0,len(string1)):
    if string1[i]==string2[0]:
        if string1[i:i+len(string2)]==string2:
                   a += 1
print("Number of times substring occured in string one is:")
print(a)
                   

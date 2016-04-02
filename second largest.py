N= input("How many numbers do you want to add in the list?")
print("Enter Numbers:")
mylist=list(map(int,input().split()))
for n in mylist:
    if n > mylist[0]:
        mylist[0],mylist[1]=n,mylist[0]
    elif mylist[0]>n>mylist[1]:
        mylist[1]=n
print("The Second largest number is:")
print(mylist[1])

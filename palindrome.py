a=input("enter the name")
for i in range(0,int(len(a)/2)):
    if a[i]==a[len(a)-i-1]:
        print("String is palindrome")
    else:
        print("it is not")
        break
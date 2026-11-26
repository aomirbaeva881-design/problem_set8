def addtwo(a,o,d):
    if o=="1":
        added=a+d
    elif o=="2":
        added=a-d
    elif o=="3":
        added=a*d
    elif o=="4":
        added=a/d
    elif o=="5":
        added="Invalid input"
    return added
a=float(input("enter first number: "))
d=float(input("enter second number: "))
c=input("enter operation: ")
x=addtwo(a,c,d)
print(x)

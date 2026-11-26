def addtwo(a,o,d):
    if o=="+":
        added=a+d
    elif o=="-":
        added=a-d
    elif o=="*":
        added=a*d
    elif o=="/":
        added=a/d
    elif o=="**":
        added=a**d
    return added
a=float(input("enter first number: "))
d=float(input("enter second number: "))
c=input("enter operation: ")
x=addtwo(a,c,d)
print(x)
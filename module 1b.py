A=int(input())
B=int(input())
C=int(input())
D=int(input())
F=int(input())
total=A+B+C+D+F
percentage=total/500*100
if percentage>=80:
    print("A")
elif percentage>=70:
    print("B")
elif percentage>=60:
    print("C")
elif percentage>=50:
    print("D")
elif percentage>=40:
    print("F")
print(total)
print(percentage)

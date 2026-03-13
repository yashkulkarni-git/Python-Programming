sub1 = int(input("enter your marks for Java : "))
sub2 = int(input("enter your marks for OS : "))
sub3 = int(input("enter your marks for RDBMS : "))
sub4 = int(input("enter your marks for DS : "))

total=sub1+sub2+sub3+sub4

percentage=total/400*100

print("Total Marks : ",total)
print("percentage : ",percentage)

if percentage >= 90:
    print("grade : A")
elif percentage >= 80:
    print("grade : B")
elif percentage >= 70:
    print("grade : C")
elif percentage >= 60:
    print("grade : D")
elif percentage >= 50:
    print("grade : E")
else:
    print("grade : F")
    

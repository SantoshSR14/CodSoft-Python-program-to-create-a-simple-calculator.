print("Enter any one option:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
a=int(input("Enter option:"))
if(a==1):
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("Sum:",b+c)
elif(a==2):
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("Difference:",b-c)
elif(a==3):
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("Product:",b*c)
elif(a==4):
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("Quotient:",b/c)
elif(a==5):
    b=int(input("Enter number 1:"))
    c=int(input("Enter number 2:"))
    print("Remainder:",b%c)
else:
    print("Invalid operation chosen")


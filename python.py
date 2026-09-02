a=10
b=3
print("addition;",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("power:",a**b)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("addition of two numbers is:",a+b)
print("subtraction of two numbers is:",a-b)
print("mutiplication of two numbers is:",a*b)
print("division of two numbers is:",a/b)
#student marks calculator
name=input("enter student name:") 
m1=int(input("enter python marks:"))
m2=int(input("enter java marks:")) 
m3=int(input("enter sQL marks:"))
total=m1+m2+m3
average=total/3
print("\n----- student Report -----")
print("Name:", name)
print("total:",total)
print("average:", average)
#shopping bill calculator
price1=float(input("Enter product 1 price:"))
price2=float(input("Enter product 2 price:"))
price3=float(input("Enter product 3 price:"))
total=price1 +price2 +price3
discount=total * 0.10
final_amount= total-discount
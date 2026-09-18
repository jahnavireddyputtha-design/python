# 1. Convert minutes
a = int(input("Enter minutes: "))

print("Hours:", a // 60)
print("Remaining minutes:", a % 60)
print("Total seconds:", a * 60)


# 2. Power calculation
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Power:", base ** exponent)


# 3. Average of three numbers
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
n3 = int(input("Enter your third number: "))

total = n1 + n2 + n3
average = total / 3

print("Total:", total)
print("Average:", average)


# 4. Greater than comparison
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Greater:", a > b)


# 5. Equality check
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

print("Both numbers are same:", n1 == n2)


# 6. Positive check
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("Both numbers are positive:", n1 > 0 and n2 > 0)


# 7. At least one even number
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("At least one number is even:", n1 % 2 == 0 or n2 % 2 == 0)


# 8. Logical NOT on a condition
num = int(input("Enter a number: "))

print("Number is not positive:", not (num > 0))


# 9. Augmented assignment operations
a = int(input("Enter a number: "))

a = a + 5
a = a * 2
a = a - 3

print("Final value:", a)


# 10. Exchange values of two variables
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


# Logic 1 - Using temporary variable
temp = a
a = b
b = temp

print("After swapping using temp:")
print(a)
print(b)


# Logic 2 - Without using temp
a = a + b
b = a - b
a = a - b

print("After swapping using + and -:")
print(a)
print(b)


# Logic 3 - Without using temp
# Using XOR
a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping using XOR:")
print(a)
print(b)


# Logic 5 - Python special method
# Simplest way
a, b = b, a

print("After swapping using Python:")
print(a)
print(b)
# calculate simple interest
# formula:(principle*rate*time)/100
#user inputs
principle=float(input("enter a decimal number:")) #loan amount
rate=float(input("enter a decimal number:"))#rate of interest
time=float(input("enter a decimal number:"))#repayment time
si=(principle *rate *time)/100
print(si)
#temperature conversion(celsius to fahrenhit)
c=float(input("enter a decimal number:"))
f=(c * 9/5)+32
print(f)
#check divisibility by 3 and 5
n=int(input("enter a number:"))
print(n%3==0 and n%5==0)
#sum of digits of a two-digit number
num=int(input("enter a number:"))#num = 4
tens=num//10 #tens=48//10=4
units=num%10 #units=48%10=8
total = tens + units#total=4+8=12
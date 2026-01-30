# Logical Operator

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(f"Is num1 greater than 10 and num2 less than 20 : {num1 > 10 and num2 < 20}")
print(f"Is num1 greater than 10 or num2 less than 20 : {num1 > 10 or num2 < 20}")
print(f"Is num1 not greater than 10 : {not num1 > 10}")
print(f"Is num2 not less than 20 : {not num2 < 20}")
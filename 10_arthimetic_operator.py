#example of arithmetic  operator
num1 = input("Enter first number")
num2 = input("Enter second number")

#convert it into integer/float 
num1 = float(num1)
num2 = int(num2) 

#process (expression) 
# expression which uses arithmetic  operator is called arithmetic expression
#variable-name = variable-name2 operator variable-name3
addition = num1 + num2 
subtraction = num1 - num2 
multiplication = num1 * num2 
division = num1 / num2 
#display 
print("addition = ",addition)
print("subtraction = ",subtraction)
print(f"multiplication = {multiplication}")
print(f"Division = {division}")

division = num1 // num2 #floor division which give answer in integer 
power = num1 ** num2 
reminder = num1 % num2 
#multiline output using \n = new line 
print(f"division = {division}\n power = {power}\n reminder = {reminder}")
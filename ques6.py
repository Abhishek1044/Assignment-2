num1 = int(input("Enter the first number: \n \t ")) 
num2 = int(input("Enter the second number: \n \t ")) 
# Using XOR function
a = bin(num1^num2) 
b = a.count('1')
print(b)
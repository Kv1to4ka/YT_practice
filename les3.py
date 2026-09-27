#УРОК 3

# print("hello world")
# some comment
'''print("5") #int
print("5.0") #float
print("Hello", 5.5, 5) 
print("world")'''
print("Hello", 5.5, 5) 
print("hello world", 5.5, 5, sep=", ")
# sep is used to separate the values with a comma and space, and end is used to specify what to print at the end of the output (in this case, an exclamation mark).
print("hello world", 5.5, 5, sep=", ", end="!")
# end is used to specify what to print at the end of the output (in this case, an exclamation mark).
print ('\n')
# \n is used to print a new line after the output.
print('\tHello')
#]t is used to print a tab space before the output.
print("John's book")
print('John\'s book')
#\' is used to escape the single quote in the string.
print("John's \\book")
#\\ is used to escape the backslash in the string.

#Математика
print(5 + 5)
print(10 - 3)
print(2 * 4)
print(10 / 2)
print(10 // 2)  # Integer division
print(10 % 2)   # Modulus (remainder)
print(2 ** 3)  # Exponentiation
print(min(5, 10, 15))  # Minimum value
print(max(5, 10, 15))  # Maximum value
print(abs(-5))  # Absolute value
print(pow(2, 3))  # Power function
print(round(3.14159, 2))  # Rounding to 2 decimal places
'''input()
input("Enter your name: ")'''
# input

print(4 ** 5)

#Урок 4

number = 5
print(number) #del number 
number = 10
print(number)
print("value", number)

num = 4.5
#float is a data type that represents decimal numbers.
num = 10
#int is a data type that represents whole numbers.
word = "Hello"
#string is a data type that represents text.
boolean = True
#boolean is a data type that can only have two values: True or False.

#невелика програма
a = input("enter num1: ")
b = input("enter num2: ")
#input() is a function that allows the user to input data. The data is stored as a string, so we need to convert it to an integer using int().
#input завжли повертає текст
print(a + b)

a = int(input("enter num1: "))
b = input("enter num2: ")
print(a +int(b))

#Урок 5
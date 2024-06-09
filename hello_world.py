
#python program
# name = input('Enter your name ',)
# print('Hi ' + name)
# number = input('Enter the number')
# print(number)

#Arithmetic operators
# num1 = input('enter the first number ')
# num2 = input('enter the second number ')

# num1 = float(num1)
# num2 = float(num2)
# print('\nThe Results\n')
# addition = print('addition\t',num1 + num2)
# subtraction = print('subtraction\t',num1 - num2)
# multiplication = print('multiplication\t', num1 * num2)
# division = print('division\t', num1 / num2)
# modulus = print('modulus\t',num1 % num2)
# exponential = print('exponential\t', num1 ** num2)
# floor_divider = print('floor_divider\t',num1 // num2)

#Assignment Operators

# a = 10
# print(a)
# b =10
# b += 10
# print(b)

#String 

# text = 'Hello World'
# multiText = """
# Hi Coders
# How are you
# Do code
# """
# word = "{} Coders"

# # print(len(text))
# # print(multiText)
# print(word.format(text))

#List

# fruits = ['Mango','Pineapple','Orange','Apple']
# print(len(fruits))
# tuple1 = ('a','b','c')
# tuple2 = ('d','e','f')
# print(tuple1 + tuple2)

#If else

# a =0
# if a >= 0:
#     if a > 0:
#      print('Positive number')
#     else:
#         print('It is zero')
# else:
#     print('It is negative number')

#while loop

# i =1
# while i<=10:
#     print(i)
#     i +=1

#functions

# def message(name):
#     print("Hello world " + name)

# def calc(num1,num2):
#     print(num1 + num2)

# def recursion(n):
#     if n <=1:
#         return n
#     else:
#         return n * recursion(n-1)

# print(recursion(3))

#class
# class Cars:
#     def __init__(self,name,color):
#         self.name  = name
#         self.color = color
#     def start(self):
#         print(self.name + ' Started')

# car1= Cars("Maruti","Red")
# car2 = Cars("Ferrari","Black")
# car1.start()

#Inheritance
class Person:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    def address(self):
        print(self.name,self.contact)

class Doctor(Person):
    pass

class Patient(Person):
    pass
 
doc1 = Doctor("Adarsh",123)

# print(doc1.name,doc1.contact)
doc1.address()

#find income

my_income = 1000
tax_rate = 0.1
my_taxes = my_income * tax_rate
# print(my_taxes)
# print(type(my_taxes))

#Strings
# a = 'hello'
# b = "a boy playing {}".format('Football')
# print(b)
# num=23.45
# print(f"My 10 character, four decimal number is:{num:{10}.{6}}"),

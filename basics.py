'''
#first practice set 
print("hello, world! welcome to python") # answer of first qustion.

print("Twinkle, twinkle, little star, \nHow I wonder what you are!") 

name="Sam"
age=18
height=5.7
is_student=True 
print("Name",name, "Age",age, "Height",height, "Student",is_student, sep="-")

num= 45
print(int(num+10))

food = input("what is your favorite food?\n")
print("Wow! I also like ", food)

number = int(input("enter a nunber\n"))
number = int(input("enter another number\n")) 
print("the answer is", number+number)
print("the answer is", number-number)
print("the answer is", number/number)
print("the answer is", number*number)

print('harry said,"python is awesome!"\nthis is a new line. \nthis is a tab ->\t<- here')

a=int(input("enter first number\n"))
print("the square is", a**2)
print("the cube is", a**3)


# second practice set
#1.(if else statements questions)
i=int(input("enter a no between \n"))
if i==0:
    print("Zero")
elif i>0:
    print("positive")
else: 
    print("negative")

age=int(input("enter your age\n"))
if age>=18:
    print("you are an adult")
else:
    print("you are not an adult")

num=int(input("enter a number\n"))
if (num%2==0): # check if the number is even or odd.
    print("even")
else:
    print("odd")

#2.(match case statements questions)
day=int(input("enter a number between 1-7\n"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 7:
        print("sunday")
    case _:
        print("no day")

num=int(input("enter a number\n"))
num2=int(input("ebter another number\n"))
operation=input("enter the operation(+,-,*,/)\n") # thisis a simple calculator using operation input in match-case statement.
match operation:
    case"+":
        print(num+num2)
    case"-":
        print(num-num2)
    case"*":
        print(num*num2)
    case"/":
        print(num/num2)

#3.(for loop questions)
for i in range (1,11):
    print(i)
 
for i in range (1,11):
    print("7 x",i,"=",7*1)

total=0
for i in range (1,101):
    print(i)
    total += i 
print("sum:", total)

for i in range (1,5):
    print("*"*i)

 # 4.(while loop qustions)
i=1
while i<=10:
    print(i)
    i+=1

sum=0
i=1
while i<=100:
    sum += i # to calculate the sum of the numbers.
    i += 1
    print(i)
print("sum of the number is:", sum)

password="admin123"
entered_password= input("enter the password\n")
while entered_password != password:
    entered_password= input("incorrect password! try again:")
print("correct passwosd! thank you")

num=876345
print(int(str(num)[::-1])) # to print the reverse of a number.

# 5.(break, continue and pass statements questions)
for i in range (1,11):
    print(i)
    if i==7:
        break

for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in range (1,6):
    match i: 
        case 1:
            print(1)
        case 2:
            print(2)
        case 3: 
            pass
        case 4:
            print(4)
        case 5:
            print(5)

# third practice set 
a ="Aanchal verma"
print(a[0:13:12])
a=len(a)
print(a)

a="anchal verma" 
print(a[0])
print(a[-1])
a=len(a)
print(a)

str1= "hello"
str2= "world"
print(str1,str2)

text = "python programming"
print(text[0:])
print(text[0:6])
print(text[13:18])
print(text[0:18:2])

text = "python programming"
print(text[0:6])
print(text[-6:])
print(text[::2])

text = "python programming"
print (text[::-1]) # it reverse the string using slicing.

text = "  i love python programming  "
print (text.strip())
print(text.title())
print(text.count("o"))

str1 = "123abc"
print (str1.isalpha()) # to check if it is alphabetic string or not 
print (str1.isalnum()) # to check if it is alphanumaric string or not 

a ="jhon"
a1 = 25
print(f"My name is {a} and I am {a1} years old")

text = "My name is {} and I am {} years old"
a = "john"
a1 = 25
s=text.format(a,a1)
print(s)

a ="jhon"
a1 = 25
print("My name is {} and I am {} years old".format(a, a1))

text = "Coding in Python is fun"
print(text)
print(text.replace("fun","awesom"))
print(text.find("Python"))

text = "Coding in Python is fun"
ind = text.index("Python")
print(ind)

text = "Coding in Python is fun"
print(text.upper())

text = "Coding in Python is fun"
sum=0
vowels = ['a','e','i','o','u']
for char in text.lower():
    if (char in vowels):
        sum+=1
print(f"The number of vowels in the sentence is= {sum}") 

str="level"
if (str == str[::-1]):
    print("this is a palindrome")
else:
    print("this is not a palindrome")

def greet():
    print("hello. Python Lerner")

greet()

def square(a):
    b=a**2
    return b 
print(square(8))

def square(x):
    return x*x
print(square(4))

def full_name(first, last):
    return f"{first} {last}"

print(full_name("Anchal", "verma"))

def calculate_area(length, width=10):
    return length * width
print(calculate_area(15))

add = lambda a, b: a + b
print (add(13, 15))

square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]
print(list(map(square, list1))

def factorial(n): 
    if n==0 or n==1:
        return 1
    return (n-1)*n

print (factorial(4))

def sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + sum_of_digits(n//10)
print(sum_of_digits(8975))

import math

a = math.sqrt(144)
b = math.sin(math.radians(90))

print(a)
print(b)

import requests 

a = requests.get("https://api.github.com/.")
print(a.json())

def increment():
    counter=0
    counter+=1
    print(counter)
increment()

def multiply(a, b):
    a = 4
    b = 9
    print(a, b)
multiply(2, 10)
'''
# def multiply(a, b):
#     '''
#     in this string we are using multiply function 
#     in this 
#     a = (int or flot) any first number
#     b = (int or flot) any second number
#     
#     and we are goinng to multiply this while using the def function
#     the function is:-
# 
#     def multiply(a, b):
#     c = a*b
#     return c (you can also right [return a*b] and skip the second step )
#     
#     print(multiply(12, 15)) [this is last step of this code and the answer will be (180)]
#         '''
#     c = a * b
#     return c
# print(multiply(12, 15))
# help(multiply)
'''
def fib(n):
    if(n==0 or n==1):
        return n
    return (fib(n-1) + fib(n-2))
print(fib(3))

def safe_divide(a, b):
    if(b==0):
        return NotImplemented
    return a/b
print(safe_divide(5,5))

def safe_divide(a, b):
    if(a==0 or b==0):
        return NotImplemented
    return a/b
print(safe_divide(5, 10))

def is_even(n):
    return n % 2==0
print(is_even(10))

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits = ["apple", "banana", "cherry"]
i = fruits.index("banana")
fruits [i] = "orenge"
print(fruits)
fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print(length)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0:3])
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[-3:])

numbers = [5,2,9,1,7]
numbers.sort()
print(numbers)
numbers = [5,2,9,1,7]
numbers.append(10)
print(numbers)
numbers = [5,2,9,1,7]
numbers.remove(2)
print(numbers)

names = ["Alice", "Bob", "charlie"]
names.insert(1,"David")
print(names)
        
coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])
coordinates = (10, 20)
# coordinates[0]=50
print(coordinates)
corlist = list(coordinates)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)

my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
my_set = {1, 2, 3, 4}
if 4 in my_set:
    print("number founded")
else:
    print("number not founded")

a = {1, 2, 3}
b = {3, 4, 5}
union = a.union(b)
intersection = a.intersection(b)
difference = a.difference(b)
print (union, intersection, difference)

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
print(student)
student["city"] = "Delhi"
print(student)

mydict = {
    "sam": 1273974923,
    "sia": 7293492839,
    "ram": 7394829373
}
print(mydict.keys())
print(mydict.values())

for key, value in mydict.items():
    print(key,"=", value)

a = [1, 2, 3, 4, 5, 6,3, 8, 4, 7, 8]
print(set(a)) # first answer 
products = {
    "apple": 0.50,
    "banana": 0.30,
    "milk": 1.20,
    "bread": 1.50,
    "eggs": 2.00
}

products = max(products.values())
print(products) # second answer 

a = {
    "name": "Alice", "age": 30, "city": "New York"}

b = {
    "product": "Laptop", "price": 1200,"brand": "Dell"}
b.update(a)
print(b) # third answer 

class car: 
    def __init__(self, name):
        self.name = name 
        print("car is moving", self.name)
c = car("BMW")
print(c.name)

class car:
    def drive(self):
        print("car is moving")
c = car()
c.drive()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("person name is", self.name, "and age is", self.age)
p = person("Anchal", 18)
'''
class Animal:
    def __init__(self, name):
        self.name = name 
    def sound(self):
        print("some sound")
a = Animal("dog")
print(a.name)
a.sound()
class Dog(Animal):
    def sound(self):
        print("woof! woof!")
d = Dog("bunny")
print(d.name)
d.sound()


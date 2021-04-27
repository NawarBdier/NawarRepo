#print("Hello World")
#age = 20
#price = 19.95
#first_name = 'Nawar'
#is_online = False
#print(age, price, first_name, is_online)
#name = input("What is your name?")
#print("Hello "+name)
#irth_year = input("Enter your birth year")

#age = 2021 - int(birth_year)
# print(age)
# float()
# bool()
# str()
"""first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("sum: "+str(sum))"""
"""course = 'Python for Beginners'
print(course.upper())
print(course)
print(course.find('y'))
print(course.replace('for', '4'))
print(course.count('o'))
print('Python' in course)"""
"""print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)"""
"""x = 10
print(x +3)
x += 3
print(x)
x = 10 + 3 * 2
print(x)
y = 3 > 2
print(y)
y = 3 == 2
print(y)
print(x > 1 and x < 20)
print(x > 1 or x < 20)
print(not x > 1)"""
"""temprature = input("enter the temprature: ")

if int(temprature) > 30:
    print("it's a hot day")
elif int(temprature) > 20:
    print("it's a nice day")
elif int(temprature) > 10:
    print("it's a bit cold")
else:
    print("it's cold")
    
print('Done')"""
"""Weight = int(input("Weight: "))
unit = input("(K)g or (L)bs? ")

if unit.upper() == "L":
    print("weight in Kg: ", Weight * 0.45)
elif unit.upper() == "K":
    converted = Weight / 0.45
    print("weight in Lbs: " + str(converted))"""
"""i = 1
while i <= 5:
    print(i * '*')
    i += 1"""
"""names = ["Nawar", "Nazeer", "Dana", "Saad"]
print(names)
print(names[1])
print(names[-2])
print(names[0:3])
number = [1, 2, 3, 4, 5]
number.append(6)
print(number)
number.insert(0, -1)
print(number)
number.remove(2)
print(number)
print(5 in number)
print(len(number))
number.clear()
print(number)"""
"""number = [1, 2, 3, 4, 5]
for item in number:
    print(item)

i = 0
while i < len(number):
    print(number[i])
    i += 1"""
"""numbers = range(5, 0, -1)
for number in numbers:
    print(number)
    number = 5"""
"""for number in range(5):
    print(number)
    number = 5"""
numbers = (1, 2, 3)
print(numbers)
print(numbers.index(3))

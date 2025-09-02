# name = "manoti"
# print ("Hello,  " + name)

# course = "Python for Beginners"
# print(course[1])

# name = "janeffer"
# print(name[1: -1])

# first = 'John'
# last = 'smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('P'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print('Python' in course)
# print(course.title())

# print(10 - 3)

# x = 10 + 3 * 2 ** 2
# print(x)

# x = (2 + 3) * 10 - 3
# print(x)

# x = 2.9
# print(round(x))
# print(abs(-2.9))

# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down payment: ${down_payment}')

# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temperature = 35
# if temperature > 30:
#     print("It;s a hot day")
# else:
#     print("it's not a hot day")
#     print("Enjoy your day")

# name = "mannnnnnnnnnnnn"
# if len(name) < 3:
#     print("Name must be atleast 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print ("Name Looks good!")

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
    
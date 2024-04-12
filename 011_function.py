def first_function():
    print("Hello World!")


first_function()

'''
This is output result

Hello World!
'''

print("-----------------------------")


def sum(a, b):
    return a + b


result = sum(1, 2)
print("Result: ", result)

'''
This is output result

Result:  3
'''

print("-----------------------------")


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


grade = calculate_grade(90)
print("Grade: ", grade)

'''
This is output result

Grade:  A
'''

print("-----------------------------")


def preview_pdf(start_page=1, end_page=100):
    print("Preview from", start_page, "to", end_page)


preview_pdf()
preview_pdf(5, 10)
preview_pdf(start_page=2, end_page=5)
preview_pdf(end_page=15, start_page=11)

'''
This is output result

Preview from 1 to 100
Preview from 5 to 10
Preview from 2 to 5
Preview from 11 to 15
'''

print("-----------------------------")


def run_command(*args):
    for arg in args:
        print("Argument: ", arg)


run_command("ping", "google.com", "-c", "3")

'''
This is output result

Argument:  ping
Argument:  google.com
Argument:  -c
Argument:  3
'''

print("-----------------------------")


def print_keyword_arguments(**keywords):
    for key in keywords:
        print(key, ":", keywords[key])


print_keyword_arguments(first_name="Jittagorn", last_name="Pitakmetagoon", occupation="Developer")

'''
This is output result

first_name : Jittagorn
last_name : Pitakmetagoon
occupation : Developer
'''

print("-----------------------------")


def lamda_function(n):
    return lambda x: x + n


f = lamda_function(10)
print("f(1): ", f(1))
print("f(2): ", f(2))
print("f(3): ", f(3))
print("f(1): ", f(1))

'''
This is output result

f(1):  11
f(2):  12
f(3):  13
f(1):  11
'''

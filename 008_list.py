numbers = [1, 2, 3, 4, 5]

print("numbers:", numbers)

'''
This is output result

numbers: [1, 2, 3, 4, 5]
'''

print("len(numbers):", len(numbers))

'''
This is output result

len(numbers): 5
'''

print("numbers[0]:", numbers[0])

'''
This is output result

numbers[0]: 1
'''

print("numbers[-1]:", numbers[-1])

'''
This is output result

numbers[-1]: 5
'''

print("numbers[1: 4]:", numbers[1: 4])

'''
This is output result

numbers[1: 4]: [2, 3, 4]
'''

numbers.append(6)
print("numbers after append(6) :", numbers)

'''
This is output result

numbers after append(6) : [1, 2, 3, 4, 5, 6]
'''

numbers[0] = 100
print("numbers after set numbers[0] = 100 :", numbers)

'''
This is output result

numbers after set numbers[0] = 100 : [100, 2, 3, 4, 5, 6]
'''

del numbers[1]
print("numbers after del numbers[1] :", numbers)

'''
This is output result

numbers after del numbers[1] : [100, 3, 4, 5, 6]
'''

new_numbers = numbers.copy()
print("new_numbers :", new_numbers)

'''
This is output result

new_numbers : [100, 3, 4, 5, 6]
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print("fruits:", fruits)
print("fruits.count('apple'):", fruits.count('apple'))
print("fruits.count('tangerine'):", fruits.count('tangerine'))
print("fruits.index('banana'):", fruits.index('banana'))
print("fruits.index('banana', 4):", fruits.index('banana', 4))  # Find next banana starting at position 4
fruits.reverse()
print("fruits.reverse():", fruits)
fruits.append('grape')
print("fruits.append('grape'): ", fruits)
fruits.sort()
print("fruits.sort(): ", fruits)
print("fruits.pop():", fruits.pop())

"""
This is output result

fruits: ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple'): 2
fruits.count('tangerine'): 0
fruits.index('banana'): 3
fruits.index('banana', 4): 6
fruits.reverse(): ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape'):  ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort():  ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop(): pear
"""

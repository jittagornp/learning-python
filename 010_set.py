basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

a = set('abracadabra')
b = set('alacazam')

print("basket:", basket)
print("'orange' in basket:", 'orange' in basket)
print("'crabgrass' in basket:", 'crabgrass' in basket)

print("a:", a)  # unique letters in a
print("b:", b)  # unique letters in b
print("a - b:", a - b)  # letters in a but not in b
print("a | b:", a | b)  # letters in a or b or both
print("a & b:", a & b)  # letters in both a and b
print("a ^ b:", a ^ b)  # letters in a or b but not both

"""
This is output result

basket: {'apple', 'pear', 'orange', 'banana'}
'orange' in basket: True
'crabgrass' in basket: False
a: {'c', 'r', 'd', 'a', 'b'}
b: {'c', 'a', 'm', 'l', 'z'}
a - b: {'d', 'r', 'b'}
a | b: {'c', 'r', 'd', 'a', 'm', 'l', 'b', 'z'}
a & b: {'c', 'a'}
a ^ b: {'m', 'r', 'b', 'l', 'd', 'z'}
"""

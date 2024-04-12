words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, ": length ", len(w))

'''
This is output result

cat : length  3
window : length  6
defenestrate : length  12
'''

print("-----------------------------")

object = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for property, value in object.copy().items():
    print(property, ":", value)

'''
This is output result

Hans : active
Éléonore : inactive
景太郎 : active
'''

print("-----------------------------")

for i in range(5):
    print("i = ", i)

'''
This is output result

i =  0
i =  1
i =  2
i =  3
i =  4
'''

print("-----------------------------")

for j in range(2, 5):
    print("j = ", j)

'''
This is output result

j =  2
j =  3
j =  4
'''

print("-----------------------------")

for n in range(10):
    if n > 5:
        break
    print("n = ", n)

'''
This is output result

n =  0
n =  1
n =  2
n =  3
n =  4
n =  5
'''

print("-----------------------------")

for m in range(10):
    if m % 2 == 0:
        continue
    print("m = ", m)

'''
This is output result

m =  1
m =  3
m =  5
m =  7
m =  9
'''

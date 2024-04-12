words = ['cat', 'window', 'defenestrate']
length = len(words)
i = 0
while i < length:
    print(words[i], ": length", str(len(words[i])))
    i = i + 1
print("-----------------------------")

'''
This is output result

cat : length  3
window : length  6
defenestrate : length  12
'''

j = 0
while True:
    print(words[j], ": length", str(len(words[j])))
    j = j + 1
    if j >= length:
        break
print("-----------------------------")

'''
This is output result

cat : length  3
window : length  6
defenestrate : length  12
'''
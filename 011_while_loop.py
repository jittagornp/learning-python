words = ['cat', 'window', 'defenestrate']
length = len(words)
i = 0
while i < length:
    print("1)", words[i], ": length", str(len(words[i])))
    i = i + 1

j = 0
while True:
    print("2)", words[j], ": length", str(len(words[j])))
    j = j + 1
    if j >= length:
        break

'''
This is output result

1) cat : length 3
1) window : length 6
1) defenestrate : length 12
2) cat : length 3
2) window : length 6
2) defenestrate : length 12
'''

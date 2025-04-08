# mydict = {
#     1: 'mek ',
#     2: 'erku ',
#     3: 'ereq ',
#     4: 'chors ',
#     5: 'hing ',
#     6: 'vec ',
#     7: 'yot ',
#     8: 'ut ',
#     9: 'iny',
#     0: 'zro '
# }

# def func(x):
#     x = str(x)
#     tiv = x.strip()
#     text = ''
#     for i in tiv:
#         text += mydict[int(i)]
#     return text


# print(func(345))

# -------------------------------------------------

# mydict = {
#     123: [201, 'Gonsales', '8:00'],
#     124: [202, 'Varduhi', '10:00'],
#     125: [203, 'Bobik', '12:00'],
#     126: [204, 'Colakich', '14:00']
# }

# def func(x):
#     return f'{x} dasyntacy ancnum e {mydict[x][0]} lsaranum, dasaxosy {mydict[x][1]}, e dasy jamy {mydict[x][2]} e'

# print(func(123))

# -------------------------------------------------


# def func(x):
#     mydict = {}
#     for i in range(x):
#         name = input('Enter name: ')
#         grade = int(input('Enter grade: '))
#         mydict[name] = grade
#     summ = 0
#     for i in mydict.values():
#         summ += i
#     maximum = float('-inf')
#     for i in mydict.values():
#         if i > maximum:
#             maximum = i
#     minimum = float('inf')
#     for i in mydict.values():
#         if i < minimum:
#             minimum = i
#     print(f"Average: {summ / len(mydict)}")
#     print(f"Maximum: {maximum}")
#     print(f"Minimum: {minimum}")

# func(3)

# --------------------------------------------------------------

# mydict = {}
# for i in range(1, 16):
#     mydict[i] = i ** 2

# print(mydict)

# --------------------------------------------------------------

# text = input('Enter a text: ')
# mydict = {}
# for i in text:
#     mydict[i] = mydict.get(i, 0) + 1
# print(mydict)

# --------------------------------------------------------------

# mydict = {
#     'awful': 'terrible',
#     'beautiful': 'pretty',
#     'great': 'excellent',
#     'generous': 'bountiful'
# }

# def func(x):
#     for key, value in mydict.items():
#         if value == x:
#             return key
#         elif key == x:
#             return value
# print(func('great'))

# --------------------------------------------------------------

# dict1 = {}
# dict2 = {}
# word1 = input('Enter a word: ')
# word2 = input('Enter a word: ')

# for i in word1:
#     dict1[i] = dict1.setdefault(i, word1.count(i))
# for i in word2:
#     dict2[i] = dict2.setdefault(i, word2.count(i))

# if dict1 == dict2:
#     print('yes')
# else:
#     print('no')


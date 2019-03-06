```python

# try:
#     age = int(input('Please enter your age: '))
#     print('I see you are %d years old. ' % age)
# except ValueError:
#     print('Hey, that wasn\'t a number!')


# def print_list_element(thelist, index):
#     try:
#         print(thelist[index])
#     except IndexError:
#         print('Index exceed!')

# print_list_element(a, 4)
# print_list_element(a, 2)
# def add(x, y): return x + y


# print(add(3, 5))
# Output: 8


import csv
import re

with open('data.csv') as f:
    reader = csv.reader(f)

    next(reader)

    data = []

    for row in reader:
        data.append(row)


# app2le

pattern = '[0-9]+'

# match = re.findall(pattern, '€110.5M78')

# print(match)

k = re.findall('[A-Z]', data[0][6])[0]
max_salary = float(re.findall(pattern, data[0][6])[0])

if k == 'K':
    max_salary = max_salary * 1000
elif k == 'M':
    max_salary = max_salary * 1000000

p = data[0][2]

print(max_salary)


for player in data:

    k = re.findall(r'[A-Z]', player[6])

    if k:
        k = k[0]

    m = float(re.findall(pattern, player[6])[0])
    if k == 'K':
        m = m * 1000
    elif k == 'M':
        m = m * 1000000
    if m > max_salary:
        max_salary = m
        p = player[2]

print('{} : {}'.format(p, max_salary))

```

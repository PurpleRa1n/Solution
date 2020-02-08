# 1
try:
    value_1 = int(input())
    value_2 = int(input())
    sum = value_1 + value_2
    print('Sum: ', sum)
    print('Diff: ', value_1 - value_2)
    print('Sum: ', sum)
except ValueError as e:
    print(e)

# 2
value = int(input())
if value % 2 == 0:
    if 2 <= value <= 27:
        print('In first range')
    print('Odd')
elif 29 <= value <= 53:
    print('In second range')
else:
    print('It\'s something')

# 3
value_1 = input()
value_2 = input()
div = value_1 / value_2
print(int(div))
print(div)

# 4
value = input()
counter = 0
tab_template = '\t'
words = value.split()
while words:
    res = ''
    while len(res) < 20:
        res = res + ' ' + words.pop(0)
    print(tab_template * counter, res)
    counter += 1
    continue

# 5
value_1 = int(input())
value_2 = [int(x) for x in input().split(', ')]
assert value_1 < len(value_2)
print(sorted(value_2, reverse=True)[:value_1])

# 6
import math

value = float(input())
print(math.pi * value)

# 7
value = input().split()
for word in reversed(value):
    print(word.lower()[::-1])

# 8
value = [int(x) for x in input().split(', ')]
while len(value) > 1:
    for idx, _ in enumerate(value):
        del value[(idx + 1) % len(value)]
print(value[0])

# 9
value_1 = int(input())
value_2 = int(input())
value_3 = int(input())
tmp = value_1 + value_2
while tmp < value_3:
    value_2, tmp = tmp, value_2 + tmp
if tmp == value_3:
    print(True)
else:
    print(False)

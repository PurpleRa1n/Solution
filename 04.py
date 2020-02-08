# 1
import datetime
date = datetime.datetime(896, 11, 13)

now = datetime.datetime.now()
delta = now - date
print(delta.days)
print(delta.days * 24)
print(delta.days * 24 * 60)

# 2
lst = [1, 2, 3]

import itertools

print(list(itertools.permutations(lst)))

# 3
import collections, operator

text = 'On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.'

counter = collections.Counter(text)
print(max(counter.items(), key=operator.itemgetter(1))[0])  # space

# 4
print([num for num in range(1000) if num % 7 == 0])

# 5
res = 0
for i in range(1, 2000):
    if len(str(i)) == 3:
        res += i
print(res)

# 6
counter = collections.Counter(text.split())
print(counter.most_common(10))

# 7
import string, random

text_length = int(input('Input length'))
lst = [
    ''.join(
        [
            random.choice(string.ascii_letters)
            for count in range(random.randint(1, 4))
        ]
    ) for i in range(text_length)
]
print(lst)

# 8
print(sorted(lst, key=lambda i: i[::-1].lower()))

# 10
lst = [[3, 5, 8], [5, 8, 10], [1, 2], [2, 13, 9]]
print(sorted(lst, key=sum, reverse=True))

# 11
lst = [
    {
        ''.join([random.choice(string.ascii_letters) for j in
                 range(random.randint(1, 5))]): [
            {
                'required': random.randint(1, 5),
                'selected': random.randint(1, 10)
            } for k in range(random.randint(1, 5))
        ]
    } for i in range(10)
]
print(lst)

# 12
lst2 = [
    m for m in [
        {
            k: v for k, v in d.items() if
            all(i['selected'] >= i['required'] for i in v)
        } for d in lst
    ] if m
]
print(lst2)

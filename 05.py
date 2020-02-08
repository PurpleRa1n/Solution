# 1
def second_max_arg(*args):
    return sorted(args)[-2]


# 2
def arg_in_dict_values(arg, dictionary):
    return arg in dictionary.values()


# 3
def sum_of_word(*args):
    digits = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10
    }
    return sum([digits[arg.lower()] for arg in args if arg in digits])


# 4
def sum_of_words(*args):
    num_map = {}

    def get_word_num(arg):
        if len(arg.split()) > 1:
            value = sum([num_map[arg] for arg in arg.split()])
        else:
            value = num_map[arg]
        return str(value)

    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]

    operators_map = {
        'plus': '+',
        'minus': '-',
        'multiply': '*',
        'divide': '/',
    }

    for idx, word in enumerate(units):
        num_map[word] = idx
    for idx, word in enumerate(tens):
        num_map[word] = idx * 10

    expr = [get_word_num(i) if i not in operators_map else operators_map[i] for
            i in args]
    return eval(''.join(expr))


# 5
import collections


def count_letters(string):
    counter = collections.Counter(
        'upper' if s.isupper()
        else 'lower' if s.islower()
        else 'punct' if s in ',.?!-'
        else 'space'
        for s in string)
    return counter.most_common()


# 6
def revser_unique(lst):
    return sorted(list(set(lst)), reverse=True)


# 7
def is_prime(num):
    if num == 1:
        return True
    elif num % 2 == 0:
        return False
    return all(num % i for i in range(2, int(num ** .5) + 1))


# 8
def is_palindrom(string):
    chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+',
             '-', '.', '!', '$', '\'', ' ', ',']
    for char in chars:
        if char in string:
            string = string.replace(char, '')
    print(string)
    return string == string[::-1]


# 9
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('Func took: ', time.time() - start)

    return wrapper()


# 10
def recursive_sum(num):
    if num == 1:
        return 1
    return num + recursive_sum(num - 1)


# 11
def recursive_mul(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] * recursive_mul(lst[1:])

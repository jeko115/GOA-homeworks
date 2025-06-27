def difference_of_squares(n):
    sum_of_numbers = sum(range(1, n + 1))
    sum_of_squares = sum(i * i for i in range(1, n + 1))
    return sum_of_numbers ** 2 - sum_of_squares

def sum_of_minimums(numbers):
    return sum(min(row) for row in numbers)

def caffeine_buzz(n):
    if n % 3 == 0 and n % 2 == 0:
        return "CoffeeScript"
    elif n % 3 == 0:
        return "JavaScript"
    else:
        return "mocha_missing!"

def rotate_matrix(arr):
    return [list(row) for row in zip(*arr[::-1])]

def check_three_and_two(array):
    from collections import Counter
    counts = Counter(array).values()
    return sorted(counts) == [2, 3]

def consonant_count(s):
    vowels = "aeiou"
    return sum(1 for c in s.lower() if c.isalpha() and c not in vowels)

def name_value(my_list):
    return [(i + 1) * sum(ord(c) - 96 for c in word.lower() if c.isalpha())
            for i, word in enumerate(my_list)]

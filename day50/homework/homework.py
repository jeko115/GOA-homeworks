def disemvowel(string_):
    vowels = "aeiouAEIOU"
    
    return ''.join([char for char in string_ if char not in vowels])



def no_space(x):
    return x.replace(" ", "")


def reverse(st):
    return st[::-1]


def add_length(str_):
    return ' '.join([word + str(len(word)) for word in str_.split()])


def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros



def remove_url_anchor(url):
    return url.split('#')[0]


def small_enough(array, limit):
    return all(x <= limit for x in array)

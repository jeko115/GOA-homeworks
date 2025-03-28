def remove_url_anchor(url):
    return url.split('#')[0]


def small_enough(array, limit):
    return all(x <= limit for x in array)


def dont_give_me_five(start, end):
    return len([n for n in range(start, end + 1) if '5' not in str(n)])


def find_it(seq):
    from collections import Counter
    counts = Counter(seq)
    
    for number, count in counts.items():
        if count % 2 != 0:
            return number



def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([1, 2, 3], [2, 3])) 
print(array_diff([1, 2, 3, 4], [4]))  


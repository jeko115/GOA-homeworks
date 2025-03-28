def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string_ if char not in vowels])




def no_space(x):
    return x.replace(" ", "")



def reverse(st):
    return st[::-1]



def add_length(str_):
    return ' '.join([word + str(len(word)) for word in str_.split()])


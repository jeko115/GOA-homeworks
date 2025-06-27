def abbrev_name(name):
    return '.'.join(word[0].upper() for word in name.split())


def dna_to_rna(dna):
    return dna.replace('T', 'U')

def is_isogram(string):
    string = string.lower()  
    return len(set(string)) == len(string)


def vowel_one(s):
    vowels = "aeiou"
    return ''.join('1' if c.lower() in vowels else '0' for c in s)

def valid_parentheses(string):
    balance = 0
    for char in string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False  
    return balance == 0  

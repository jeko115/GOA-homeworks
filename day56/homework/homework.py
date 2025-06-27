def DNA_strand(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        next_root = int(root) + 1
        return next_root ** 2
    else:
        return -1

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())

def double_every_other(lst):
    return [x * 2 if i % 2 == 1 else x for i, x in enumerate(lst)]

def tail_swap(strings):
    a, b = strings
    
    mid_a = len(a) // 2
    mid_b = len(b) // 2
    
    new_a = a[:mid_a] + b[mid_b:]
    new_b = b[:mid_b] + a[mid_a:]
    return [new_a, new_b]

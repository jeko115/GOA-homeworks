def duplicate_encode(word):
    word = word.lower()  # პატარა ასოებად ვაქცევთ
    return ''.join('(' if word.count(c) == 1 else ')' for c in word)

def find_nb(m):
    n = 0
    total = 0
    while total < m:
        n += 1
        total += n**3
    return n if total == m else -1

def find_missing_letter(chars):
    for i in range(len(chars)-1):
        # თუ უახლოეს ასოებს შორის სხვაობა > 1ა, ეს ნიშნავს აკლია ასო
        if ord(chars[i+1]) - ord(chars[i]) > 1:
            return chr(ord(chars[i]) + 1)
    return None  # თუ არაფერი არ აკლია

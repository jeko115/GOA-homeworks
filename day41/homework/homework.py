def summation(num):
    return sum(range(1, num + 1))

# Examples
print(summation(2))  # 3 (1 + 2)
print(summation(8))  # 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)



def count_sheep(sheep):
    return sum(sheep)

# Example
sheep_list = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]

print(count_sheep(sheep_list))  # 17




def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return "Invalid operator"

# Examples
print(basic_op('+', 4, 7))   # 11
print(basic_op('-', 15, 18)) # -3
print(basic_op('*', 5, 5))   # 25
print(basic_op('/', 49, 7))  # 7.0





def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

# Example
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))  
# Output: "found the needle at position 5"

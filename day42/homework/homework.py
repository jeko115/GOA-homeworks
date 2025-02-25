def dot_calculator(equation):
    left, operator, right = equation.split()
    left_count = len(left)
    right_count = len(right)

    # Perform the calculation
    if operator == '+':
        result = left_count + right_count
    elif operator == '-':
        result = left_count - right_count
    elif operator == '*':
        result = left_count * right_count
    elif operator == '//':
        result = left_count // right_count
    else:
        return "Invalid operator"

    # Return the result as dots (or empty string if 0)
    return '.' * result

# Examples
print(dot_calculator("..... + ..............."))  # "...................."
print(dot_calculator("..... - ..."))  # ".."
print(dot_calculator("..... * .."))  # ".........."
print(dot_calculator("..... // .."))  # ".."
print(dot_calculator(". // .."))  # ""





def disemvowel(string):
    vowels = "aeiouAEIOU"
    return "".join(char for char in string if char not in vowels)

# Example
print(disemvowel("This website is for losers LOL!"))  # "Ths wbst s fr lsrs LL!"



def solution(string, ending):
    return string.endswith(ending)

# Examples
print(solution('abc', 'bc'))  # True
print(solution('abc', 'd'))   # False

def replace_vowels(s):
    return "".join("!" if char in "aeiouAEIOU" else char for char in s)

# Example tests
print(replace_vowels("Hi!"))         # "H!!"
print(replace_vowels("!Hi! Hi!"))    # "!H!! H!!"
print(replace_vowels("aeiou"))       # "!!!!!"
print(replace_vowels("ABCDE"))       # "!BCD!"



def derive(coefficient, exponent):
    result = coefficient * exponent  # Multiply coefficient by exponent
    new_exponent = exponent - 1      # Subtract 1 from exponent
    return f"{result}x^{new_exponent}"  # Format the output as a string

# Example tests
print(derive(7, 8))  # Output: "56x^7"
print(derive(5, 9))  # Output: "45x^8"
print(derive(3, 2))  # Output: "6x^1"
print(derive(4, 5))  # Output: "20x^4"




def get_weekday(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(num, "Wrong, please enter a number between 1 and 7")

# Example tests
print(get_weekday(1))  # Output: "Sunday"
print(get_weekday(5))  # Output: "Thursday"
print(get_weekday(7))  # Output: "Saturday"
print(get_weekday(9))  # Output: "Wrong, please enter a number between 1 and 7"
print(get_weekday(0))  # Output: "Wrong, please enter a number between 1 and 7"

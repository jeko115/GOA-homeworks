def no_space(text):
    return text.replace(" ", "")

# Examples
print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))  # "8j8mBliB8gimjB8B8jlB"
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))  # "88Bifk8hB8BB8BBBB888chl8BhBfd"
print(no_space("8aaaaa dddd r     "))  # "8aaaaaddddr"




import math

def litres(time):
    return math.floor(time * 0.5)

# Examples
print(litres(3))    # 1
print(litres(6.7))  # 3
print(litres(11.8)) # 5



def digitize(n):
    return [int(digit) for digit in str(n)][::-1]

# Examples
print(digitize(35231))  # [1, 3, 2, 5, 3]
print(digitize(0))      # [0]

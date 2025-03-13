def litres(time):
    return int(time * 0.5)

# ტესტები:
print(litres(3))    # 1
print(litres(6.7))  # 3
print(litres(11.8)) # 5




def lovefunc(flower1, flower2):
    return (flower1 % 2) != (flower2 % 2)

# Example usage:
print(lovefunc(4, 7))  # True
print(lovefunc(2, 4))  # False
print(lovefunc(3, 5))  # False
print(lovefunc(1, 8))  # True

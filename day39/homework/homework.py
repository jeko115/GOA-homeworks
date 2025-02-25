def repeat_string(n, s):
    return s * n

# Examples
print(repeat_string(6, "I"))      # "IIIIII"
print(repeat_string(5, "Hello"))  # "HelloHelloHelloHelloHello"



def sum_array(arr):
    return sum(arr)

# Examples
print(sum_array([1, 5.2, 4, 0, -1]))  # 9.2
print(sum_array([]))                  # 0
print(sum_array([-2.398]))             # -2.398



def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

# Examples
print(square_sum([1, 2, 2]))  # 9
print(square_sum([0, 3, 4, 5]))  # 50
print(square_sum([]))  # 0
print(square_sum([-1, -2]))  # 5

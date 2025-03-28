def find_multiples(n, limit):
    return [i for i in range(n, limit + 1, n)]

# Example usage:
print(find_multiples(2, 6))  # Output: [2, 4, 6]
print(find_multiples(3, 10))  # Output: [3, 6, 9]
print(find_multiples(5, 25))  # Output: [5, 10, 15, 20, 25]



def multiples(x, n):
    return [x * i for i in range(1, n + 1)]

# Example usage:
print(multiples(2, 5))  # Output: [2, 4, 6, 8, 10]
print(multiples(3, 4))  # Output: [3, 6, 9, 12]
print(multiples(5, 3))  # Output: [5, 10, 15]

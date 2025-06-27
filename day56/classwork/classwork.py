# ფუნქცია რომელიც აბრუნებს 1-დან n-მდე ყველა რიცხვის ჯამს
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# ფუნქციის გამოძახება 3 სხვადასხვა რიცხვზე
print("Sum to 5:", sum_to_n(5))    # 1 + 2 + 3 + 4 + 5 = 15
print("Sum to 10:", sum_to_n(10))  # 55
print("Sum to 100:", sum_to_n(100))  # 5050

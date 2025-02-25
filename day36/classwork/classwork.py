def check_product(a, b):
    product = a * b
    parity = "ლუწია" if product % 2 == 0 else "კენტია"
    print(f"ნამრავლი: {product}, {parity}")

# ფუნქციის გამოძახება სხვადასხვა არგუმენტებით
check_product(4, 5)   # 20, ლუწია
check_product(3, 7)   # 21, კენტია
check_product(6, 2)   # 12, ლუწია
check_product(9, 9)   # 81, კენტია

def calculate_discount(price, discount_percent):
    if discount_percent <= 20:
        return price
    return float(price) * (discount_percent)

price = input("What is the price: ")
dicount = float(input("Enter discount: "))
print(calculate_discount(price,dicount))
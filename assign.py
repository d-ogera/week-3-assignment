def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
try:
    original_price = float(input("Please enter the original price of the item: "))
    discount_percent = float(input("Now enter the discount percent: "))

    final_price = calculate_discount(original_price, discount_percent)
    if final_price == original_price:
        print(f"Ooops! No discount applied. Your final price is: {final_price:.2f}")
    else:
        print(f"Wow! A discount applied. Your final price is: {final_price:.2f}")
except ValueError:
    print("Please use correct values")

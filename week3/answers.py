def calculate_discount(original_price, discount_percent):

    original_price = float(original_price)
    discount_percent = float(discount_percent)

    if discount_percent > 99:
        return 'Execution terminated. Wrong discount_percent'

    if discount_percent >= 20:
        discount = original_price * (discount_percent/100)
        final_price = original_price - discount
        return final_price
    else:
        return original_price
    
original_price = input('Enter item price...:\n')
discount_percent = input("Enter the discount percentage...:\n")

print("Final Price: ", calculate_discount(original_price, discount_percent))
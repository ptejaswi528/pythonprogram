import ecommerce_utils

def add_to_cart(cart, product, price):
    if product in cart:
        print(f"'{product}' is already in the cart. Use update if you want to change the price.")
    else:
        cart[product] = price
        print(f"'{product}' added to cart.")
    return cart

def display_invoice(cart, discount_percent, gst_percent):    
    if not cart:
        print("\nYour shopping cart is empty.")
        return
    total, after_discount, after_gst = ecommerce_utils.generate_invoice(
        cart, discount_percent, gst_percent
    )

    print("\n-------INVOICE-------")
    for product, price in cart.items():
        print(f"{product:<15} | Rs. {price}")
    print("-----------------------")
    print(f"{'Total Price':<15} | Rs. {total:.2f}")
    print(f"{'After Discount':<15} | Rs. {after_discount:.2f} ({discount_percent}%)")
    print(f"{'Final Amount (inc. GST)':<15} | Rs. {after_gst:.2f} ({gst_percent}%)")
    print("-----------------------")
cart = {}
DISCOUNT = 10  
GST = 18       
while True:
    print("\n1. Add item to cart")
    print("2. Generate Invoice and Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        product = input("Enter product name: ")
        try:
            price = int(input("Enter price: "))
            cart = add_to_cart(cart, product, price)
        except ValueError:
            print("Invalid price. Please enter a number.")
    
    elif choice == '2':
        break
    else:
        print("Invalid choice, please try again.")
display_invoice(cart, DISCOUNT, GST)
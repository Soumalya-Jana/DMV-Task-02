# This function generates a receipt for a purchase, given the item name, price, and quantity.
def generate_receipt(item_name, price, quantity):
    total_cost = price * quantity
    print("--- RECEIPT ---")
    print(f"Item: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total_cost:.2f}")
    print("---------------")

generate_receipt("Wireless Mouse", 24.99, 2)
generate_receipt("Coffee Mug", 12.50, 4)
# This function checks if an item is available in stock based on the stock count.
def check_item_availability(stock_count):
    if stock_count <= 0:
        return False
        
    print("Item is in stock. Processing shipping options...")
    return True

is_available = check_item_availability(0)
print(f"Can I buy this? {is_available}")  
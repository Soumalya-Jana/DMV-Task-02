# This function converts an amount in USD to EUR using a mock exchange rate.
def convert_usd_to_eur(usd_amount):
    exchange_rate = 0.92  # Mock exchange rate
    eur_amount = usd_amount * exchange_rate
    return eur_amount

# Capture the return value
my_euros = convert_usd_to_eur(100)
print(f"You have €{my_euros:.2f}") 
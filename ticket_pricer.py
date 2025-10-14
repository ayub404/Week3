age = int(input('Whats your age: '))
price = []
category = []
if age <= 12:
    price = 8
    category = 'Children'
elif age >= 64:
    price = 15
    category = 'Adults'
    
else:
    price = 10
    category = 'Seniors'


print(f"\n--- Movie Ticket Pricer ---")
print(f"Your age is: {age}")
print(f"You fall into the {category} category.")
print(f"Your ticket price is: ${price}")


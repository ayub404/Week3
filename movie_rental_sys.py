print(f'''\n\n=== Streaming Movie Rental System ===
Enter rental period: 24hour, 48hour, or weekly
Type  when finished selecting movies''')
subtotal = float()
prices = 3.99, 5.99 , 8.99
discount = 3.50

while True:
    period = input('Enter rental period: ')
    if period.lower() == 'done':
        break

    if period.lower() == '24hour' or period.lower() == '24 hour':
        price = prices[0]
        subtotal += price
        print(f'Price: {price}')
        print(f'Current total: {subtotal}\n')
    elif period.lower() == '48hour' or period.lower() == '48 hour':
        price = prices[1]
        subtotal += price
        print(f'Price: {price}')
        print(f'Current total: {subtotal}\n')
    elif period.lower() == 'weekly':
        price = prices[2]
        subtotal += price
        print(f'Price: {price}')
        print(f'Current total: {subtotal}\n')
    else:
        print('Please check your input!')

# === Rental Summary ===
# Subtotal: $28.95
# Binge Watcher Discount: -$3.50
# Final Total: $25.45
# Thank you for your rental!

if subtotal < 25:
    discount = 0
    

print(f'''
=== Rental Summary ===
Subtotal: ${subtotal:.2f}
Binge Watcher discount: ${discount:.2f} 
Final Total: {subtotal - discount:.2f} 
Thank you for your rental!''')
print('\n\n=== Streaming Movie Rental System ===')
print('Enter rental period: 24hour, 48hour, or weekly')
print('Type "done"  when finished selecting movies')
subtotal = float()

discount = 3.50

while True:
    period = input('Enter rental period: ')
    if period == 'done':
        break

    if period == '24hour' or period == '24 hour':
        price = 3.99
        subtotal += price
        print(f'Price: {price}')
        print(f'Current total: {subtotal}\n')
    elif period == '48hour' or period == '48 hour':
        price = 5.99
        subtotal += price
        print(f'Price: {price}')
        print(f'Current total: {subtotal}\n')
    elif period == 'weekly':
        price = 8.99
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
    
print('=== Rental Summary ===')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Binge Watcher discount: ${discount:.2f} ')
print(f'Final Total: {subtotal - discount:.2f} ')
print(f'Thank you for your rental!')

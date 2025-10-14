
count = 0
current_total = float()

while True:
    num = (input("Enter the number or 'done' to stop: "))
    
    if num.lower() == 'done':
        break
        
    numbers = float(num)
    current_total += numbers
    count +=1

    print(f"Current total is: {current_total:.1f}")

    print(f"Number of numbers: {count}")

print(f"Current total is: {current_total}")
print(f'Numbers of participated numbers: {count}')
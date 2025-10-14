height = int(input('Enter its height: '))

for i in range(1, height + 1):
    
    for j in range(i):
        print('*', end = ' ')
        print(j, end = '  ')
    
    print()


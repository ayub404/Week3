number = int(input('How many Fibonacci numbers would you like to generate? '))
a,b = 0,1
for i in range(0,number ):
    print(a, end = ' ')
    a,b = b, a+b
   
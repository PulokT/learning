largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == ('done'): #take input untill 'done' is entered. 
        break
    try:
        num1=int(num)
        
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = num1
    elif num1 < smallest:
        smallest = num1
    if largest is None:
        largest = num1
    elif num1 > largest:
        largest = num1
print('Maximum is',largest)
print('Minimum is',smallest)
        
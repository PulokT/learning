# def greet(lang):
#     if lang == 'es':
#         print('Hola')
#     elif lang == 'fr':
#         print ('Bonjour')
#     else:
#         print('Hello')
# greet ('es')


# def greet():
#     return 'Helo'
# print(greet() , 'Glenn' )
# print(greet(),'Max')


# def greet(lang):
#     if lang=='es':
#         return 'Hola'
#     elif lang=='fr':
#         return 'Bonjour'
#     else:
#         return 'hello'
# print (greet('fr'), 'Pulok')
# print (greet('jp'), 'Pulok')


# def y(a,b):
#     x = a+b
#     return x

# z = y(3,5)
# print(z)

# def multiplyby2 (num):
#     return num*2
# y=float(input('Enter a number: '))
# result = multiplyby2 (y)
# print (result)

#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
def computepay(h,r):
    if h>=40:
        hh=h-40
    return (40*r + hh*r*1.5)

h=float(input("Enter Hours:"))
r=float(input("Enter Rate: "))
p = computepay(h,r)
print("Pay",p)
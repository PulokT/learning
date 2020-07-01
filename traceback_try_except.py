pulok = input('Enter a number: ')
try:
    x = int(pulok)
except:
    x = -1
if x > 0:
    print('Nice job')
else:
    print('Not a number')

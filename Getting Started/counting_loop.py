i=0
sum = 0
print('Before', i)
for thing in [9,11,12,3,12,2,2,2,2,2,2,2,2,2,3,55,5,32,1,312,213,21,3,321,213,123,231,23]:
    i=i+1
    sum = sum + thing
    print(i, thing)
print('After:', 'count: '+str(i)+',', 'sum: '+str(sum)+',', 'average: '+str(sum/i)+'!')

found = False
print('Before', found)
for value in [91, 411, 128, 3, 83,  4, 34]:
    if value == 3:
        found = True
    print (found, value)
print('After', found)

num =  0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == ('done'):
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue    
    print(fval)
    num = num + 1
    tot = tot + fval

print('ALL DONE')
print('total: '+str(tot)+',','count: '+str(num)+',','average: '+str(tot/num)+'!')


# largest_so_far = -1
# #print ('Before', largest_so_far)

# for the_num in [9, 41,100,17398127938172, 898989846545646546546546546546546546546546546546546564656, 1830912839012830912830912, 172893981273981273, 17983712983719837, 1283091283091823098129038019238, 1892387928309128309128309183091830912, 12093192039021830912830912830812093, 21338109381092380129839023]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     #print(largest_so_far, the_num)
# print('largest:', largest_so_far)


smallest = None
largest = None
#print ('Before')
for value in [1,2,-1,-500,6,834,5345,633,6,66,234]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    #print(smallest,value)
print('smallest:',smallest)
print('largest:',largest)
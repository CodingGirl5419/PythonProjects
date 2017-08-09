list = [1, 2, 3, 4, 5, 6, 7]


#middle = list[0] + list[6] / 2

#for item in list:
#    list[0] + list[6] / 2
    #if item in list > middle
#    print(list)

def binarysort(list, x):
    first = 0
    last = len(list)-1
    Found = False

    while Found == False:
        midpoint = int((first+last) / 2)
        if list[midpoint]== x:
            Found == True
        elif list[midpoint] < x:
            last = midpoint
        else:
            first = midpoint
print(binarysort(list, 3))

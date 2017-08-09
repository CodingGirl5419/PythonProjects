myList = [5, 4, 30, 2 , 1]

def sort(list):
    for ite in range(5):
        i = 0
        for item in list:
            if i < 4:
                a = list[i]
                j = i + 1
                b = list[j]
                if (a > b):
                    list[i] = b;
                    list[j] = a;
                i = i+1
    print(list)

sort(myList);

#if myList[0]>myList[1, 2, 3, 4]:
    #myList[4, 3, 2, 1, 0]
    #print(myList)

#for item in myList();
    #if item >[0];
    #item <[0]
    #print(myList)

#for item in range(4);
    #myList(item-1);
    #print(myList)

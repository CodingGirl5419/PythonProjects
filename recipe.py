dict = {
    "crushed cookies": 14,
    "crushed peanut butter cups": 15,
    "candy-coated chocolate pieces": "1 cup",
    "vanilla ice cream": "1/2 gallon",
    "5-ounce paper cups": 15
    }

myList = ["Combine the crushed cookies, peanut butter cups and candy-coated chocolate pieces", "add a spoonful to the bottom of each paper cup", "Scoop the ice cream into a large bowl of a mixer", "Pour in the remaining chocolate-cookie mix", "Mix gently with a paddle attachment", "Spoon the ice cream into the cups and carefully insert a popsicle stick into each pop", "Freeze until the ice cream has solidified. Tear off the paper cups to serve"]

#print (myList[0])
#print (myList[1])
#print (myList[2])
#print (myList[3])
#print (myList[4])

print ("dict['crushed cookies']: ", dict["crushed cookies"])
print ("dict['crushed peanut butter cups']: ", dict["crushed peanut butter cups"])
print ("dict['candy-coated chocolate pieces']: ", dict["candy-coated chocolate pieces"])
print ("dict['vanilla ice cream']: ", dict["vanilla ice cream"])
print ("dict['5-ounce paper cups']: ", dict["5-ounce paper cups"])

for i in range(4):
    print (myList[i])

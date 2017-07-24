start = '''
You receive a text from your friend in the middle of the night, but you should already be asleep.
Your curfew is at 10:00 PM and you're already grounded for breaking your curfew twice.
You either choose to hang out with your friend and 'sneak out' or 'stay home'.
'''


print(start)


print("Type 'sneak out' to sneak out or 'stay home' to stay home.")
user_input = input()
if user_input == "sneak out":
    print("You decide to sneak out and come across your sleeping dog.")
    print("Type 'tip toe' to tip toe or 'run' to run.")
elif user_input == "stay home":
    print("You choose to stay home and miss out an epic night out. You lose.")
user_input = input()
if user_input == "tip toe":
    print("You managed to sneak past your dog, but then come across your mom in the kitchen. You can either wait until she leaves or wait until she's not looking and make a run for it.")
    print("Type 'wait until she's gone' to safely make a run for it or 'wait until she's not looking' to make a run for it.")
elif user_input == "run":
    print("Your dog barks and wakes up your parents. So you lose!")
user_input = input()
if user_input == "wait until she's gone":
    print("Congratulations! You managed to sneak out with your friend!")
elif user_input == "wait until she's not looking":
    print("You lose! You got caught by your mom.")

else:
    choiceNotMade = True
    while choiceNotMade:
        print("Incorrect input! Pick one of the choices given to you.")

        print("Type 'sneak out' to sneak out or 'stay home' to stay home.")
        user_input = input()
        if user_input == "sneak out":
            print("You decide to sneak out and come across your sleeping dog.") # finished the story by writing what happens
            choiceNotMade = False
        elif user_input == "stay home":
            print("You choose to stay home and nothing happens. You sleep, missing out on an epic night out. You lose.") # finished the story writing what happens
            choiceNotMade = False

start = '''
You receive a text from your friend in the middle of the night, but you should already be asleep.
Your curfew is at 10:00 PM and you're already grounded for breaking your curfew twice.
You either choose to hang out with your friend and 'sneak out' or 'stay home'.
'''


print(start)


print("Type 'sneak out' to sneak out or 'stay home' to stay home.")
user_input = input()
if user_input == "sneak out":
    print("You decide to sneak out and come across your sleeping dog.")
    print("Type 'tip toe' to tip toe or 'run' to run.")
elif user_input == "stay home":
    print("You choose to stay home and miss out an epic night out. You lose.")
#else:
    # choiceNotMade = True
     #while choiceNotMade:
        #print("Incorrect input! Pick one of the choices given to you.")
     #user_input = input()
     #if user_input == "sneak out":
             #print("You decide to sneak out and come across your sleeping dog.") # finished the story by writing what happens
             #choiceNotMade = False
     #elif user_input == "stay home":
             #print("You choose to stay home and nothing happens. You sleep, missing out on an epic night out. You lose.") # finished the story writing what happens
             #choiceNotMade = False
user_input = input()
if user_input == "tip toe":
    print("You managed to sneak past your dog, but then come across your mom in the kitchen. You can either wait until she leaves or wait until she's not looking and make a run for it.")
    print("Type 'wait until she's gone' to safely make a run for it or 'wait until she's not looking' to make a run for it.")
elif user_input == "run":
    print("Your dog barks and wakes up your parents. So you lose!")
user_input = input()
if user_input == "wait until she's gone":
    print("Congratulations! You managed to sneak out with your friend!")
elif user_input == "wait until she's not looking":
    print("You lose! You got caught by your mom.")
else:
    print("Tap enter twice to restart after losing or incorrect input.")
# else:
#     choiceNotMade = True
#     while choiceNotMade:
#         print("Incorrect input! Pick one of the choices given to you.")
#
#         print("Type 'sneak out' to sneak out or 'stay home' to stay home.")
#         user_input = input()
#         if user_input == "sneak out":
#             print("You decide to sneak out and come across your sleeping dog.") # finished the story by writing what happens
#             choiceNotMade = False
#         elif user_input == "stay home":
#             print("You choose to stay home and nothing happens. You sleep, missing out on an epic night out. You lose.") # finished the story writing what happens
#             choiceNotMade = False

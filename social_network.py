class User:
    # Define the fields and methods for your object here.
    def __init__(self, name, password):
        self.user_name = name
        self.friends = []
        self.pass_word = password


    def change_user_name(self, name):
        self.user_name = name

    def change_pass_word(self, password):
        self.pass_word = password

    def add_friends(self, friends):
        self.friends.append(friends)

    def deletefriends(self, friends):
        self.friends.remove(friends)

    def getuser_name(self):
        return self.user_name

    def getpass_word(self):
        return self.pass_word

    def getfriends(self):
        return self.friends


class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.all_users = []

    def addallUsers(self, user):
        if user is not Network:
            self.all_users.append(user)
        else:
            print("this username is already taken")

    def addConnectionNet(self, user1, user2):
        if user2 is not user1.friends:

            user1.friends.append(user2)
            user2.friend.append(user1)
        else:
            print("You are already connected to this user")

    def getall_users(self, allUsers):
        self.all_users = []

    def changeprofile(self, profile):
        self.profile = profile

    def getprofile(self):
        return self.profile

    def getConnectionNet(self, user1, user2):
        return self.ConnectionNet


def main():
    # Define the program flow for your user interface here.
    print("----------------------------------------")
    input("Press 'y' if you want to make an account")
    print("----------------------------------------")

    y1 = input("Username:")
    y2 = input("Password:")

    newUser = User(y1, y2)

    otherUser = User("alex", "123")

    #if input == y:
        #y = input("Username:")
        #y = input("Password:")
        #password = input("Password:")
        #if password == password:
                #print("Your passwords do not match")
    myNetwork = Network()
    myNetwork.addallUsers(newUser)
    myNetwork.addallUsers(otherUser)
    myNetwork.getall_users(newUser, otherUser)
    print("Welcome!", y1, "!")

    print("------------------------------")
    input("Type 'add user' to add a user")
    print("------------------------------")
    input("Type the name of the user to add them")
    print("-------------------------------------")
    #user2 = ("cat")
    myNetwork.addConnectionNet(newUser, otherUser)




#print("type in your username")
#print("type in your password")
#print("Who do you want to connect to?")
# Runs your program.
if __name__ == '__main__':
    main()

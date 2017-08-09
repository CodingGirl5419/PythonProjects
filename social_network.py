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

    def getuser_name(self):
        return self.user_name

    def getpass_word(self):
        return self.pass_word

    def getfriends(self):
        return self.friends

    def getprofile(self):
        return self.profile


class Network:
    # Define the fields and methods for your object here.
    def __init__(self, allUsers, profile):
        self.profile = profile
        self.all_users = allUsers

    def changeprofile(self, profile):
        self.profile = profile

    def getprofile(self):
        return self.profile


def main():
    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
    main():

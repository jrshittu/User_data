# import time
import time

# create an empty dictionary
users = {}

# create an empty string for status
status = ""

# create the function
def main_menu():
    global status
    
    status = input("Do you have a login account? y/n or press q to quit. ")
    
    # define the conditions for old, new and uninterested user
    if status == "y":
        print("Welcome Back")
        current_user()
        
    elif status == "n":
        print("You found the right choice")
        new_user()
        
    elif status == "q":
        print("So sad to see you go, We are going to miss you")
        quit()
            
def new_user():
    create_login = input("Create a user name: ")
    
    if create_login in users:
        print("\nName already taken, please choose another one\n")
        
    else: 
        create_passkey = input("Create Password: ")
        users[create_login] = create_passkey
        print("\nUser Created!\n")
        logins = open("/Users/Zayn/Documents/User_data/Hello.txt", "a")
        logins.write("\n" + "Username: " + create_login + ", Password: " + create_passkey)
        logins.close()
    
def current_user():
    username = input("Kindly enter your Username: ")
    passkey = input("Kindly enter your Password: ")
    
    # check if the user is already registered 
    if username in users and users[username] == passkey:
        print("\n You\'re Welcome")
        print("User: ", username, "accessed the system on: ", time.asctime())
    
    else:
        print("\n Incorrect password or username")
 
 
while status != "q":
    main_menu()
     
    
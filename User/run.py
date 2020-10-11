#!/usr/bin/env python3.6
from user import User

def create_user(details,logname,password):
    """
    Function to create a new user
    """
    
    new_user = User(details,logname,password)
    return new_user


def save_users(user):
    """
    Function to save user
    """
    
    user.save_user()
    
    
def del_contact(contact):
    """
    Function to delete a user
    """
    
    user.delete_user
    
    
def find_user(details):
    """
    Function that finds a user by details and return the user
    """
    
    return User.find_by_details(details)


def check_existing_users(details):
    """
    Function to check if an user exists with the details and returns a Boolean
    """
    
    return User.user_exists(details)


def display_users():
    """
    Function that returns all the saved users
    """
    
    return User.display_users()     


def main():
    print("Hey Welcome to your Password Locker.Please enter your name")
    user_name = input()
    
    print(f"Hey {user_name}. What would you like to do?")
    print('/n')
    
    while True:
        print("Use these short codes: nu - create a new user, du - display users, fu - find user, ex - exit user list")
       
        short_code = input().lower()
        
        if short_code == 'nu':
            print("New User")
            print("-"*10)
            
            print ("Details ....")
            details = input()
            
            print ("login_username ....")
            logname = input()
            
            print ("password ....")
            password = input()
            
            save_users(create_user(details,logname,password))
            
            print ('\n')
            print(f"New User {details} {logname} {password} created")
            print ('\n')
            
            
        elif short_code == 'du':
            
            if display_users():
                print("Here are the informations from the user list")
                print('\n')
                
                for user in display_users():
                    print(f"{user.details} {user.login_username} {user.password}")
                    
                    print('\n')
                    
            else:
                print('\n')
                print("You don't seem to have any passwords saved yet")
                print('\n')
                
        
        elif short_code == 'fu':
            print("Enter the details for the password you want to find")
            
            search_details = input()
            
            if check_existing_users(search_details):
                search_user = find_user(search_details)
                print(f"{search_user.login_username}")
                
                print('-'* 20)
                
                print(f"Details..... {search_user.details}")
                
                print(f"Password..... {search_user.password}")
                
            else: 
                print("That detail does not exist")
                
                
        elif short_code == 'ex':
            print("Great Day ......")
            break
        
        
        else: 
            print("Please use the short codes.")
             
# if __name__ == '__main__':
#     main()
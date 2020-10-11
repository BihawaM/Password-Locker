# import pyperclip
class User:

    """
    Class that generates new instances of users.
    """
    
    user_list = []
    
    
    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        
        User.user_list.append(self)
        
        
    def __init__(self,details,login_username,password):
        
        self.details = details
        self.login_username = login_username
        self.password = password
        
    
    def delete_user(self):
        """
        delete_user method deletes a saved user from the user_list
        """
        
        User.user_list.remove(self)
        
        
    @classmethod
    def find_by_details(cls,details):
        """
        Method that takes in a details and returns a user that matches the details.
        
        Args: 
            details: details to search for
        Returns:
            Details of user that matches the details.     
        """
        
        for user in cls.user_list:
            if user.details == details:
                return user
        
        
    @classmethod
    def user_exists(cls,details):
        """
        Method that checks if a user existsfrom the user list.
        Args:
            details: details to search if it exists
        Returns:
            Boolean: True or false depensing if the user exists.     
        """
        
        for user in cls.user_list:
            if user.details == details:
                return True
            
        return False
    
    
    @classmethod
    def display_users(cls):
        """
        returns the user list
        """
        
        return cls.user_list
    
    
    
    # @classmethod
    # def copy_password(cls,details):
    #     user_found = User.find_by_details(details)
    #     pyperclip.copy(user_found.password)    
                
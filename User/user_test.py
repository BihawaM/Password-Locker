# import pyperclip
import unittest
from user import User 


# class TestUser(unittest.TestCase):
#     """
#     Test class that defines test cases for the user class behaviours.
#     """
    
    
#     def setUp(self):
#         """
#         Set up method to run before each test case
#         """
        
#         self.new_user = User("Instagram password","Bello_Murray","pass1234#")
        
    
#     def test_init(self):
#         """
#         test_init test case to test if the object is initialized properly
#         """
        
#         self.assertEqual(self.new_user.details,"Instagram password")
#         self.assertEqual(self.new_user.login_username,"Bello_Murray")
#         self.assertEqual(self.new_user.password,"pass1234#")
        
        
#     def test_save_user(self):
#         """
#         test_save_user test case to test if the user object is saved into the user list
#         """
        
#         self.new_user.save_user()
#         self.assertEqual(len(User.user_list),1)     
        
        
#     def tearDown(self):
#         """
#         tearDown method that does clean up after each test case has run
#         """
        
#         User.user_list = []
        
     
#     def test_save_multiple_user(self):
#         """  
#         test_save_multiple_user checks if we can save multiple user objects to our user_list
#         """
        
#         self.new_user.save_user()
#         test_user = User("Facebook password","Bihawa Mohamed","65432*")
#         test_user.save_user()
#         self.assertEqual(len(User.user_list),2)
        
        
#     def test_delete_user(self):
#         """
#         test_delete_user tests if we can remove a contact from our contact list
#         """
        
#         self.new_user.save_user()
#         test_user = User("Facebook","Bihawa Mohamed","65432*")
#         test_user.save_user()
        
#         self.new_user.delete_user()
#         self.assertEqual(len(User.user_list),1)
        
        
#     def test_find_user_by_details(self):
#         """
#         test to check if we can find a user by details and display information
#         """
        
#         self.new_user.save_user()
#         test_user = User("WhatsApp password","Bihawa Mohamed","65432*") 
#         test_user.save_user()
        
#         found_user = User.find_by_details("WhatsApp password")
        
#         self.assertEqual(found_user.password,test_user.password)   
        
        
#     def test_user_exists(self):
#         """
#         test to check if we can return a Boolean if we can't find the user.
#         """
        
#         self.new_user.save_user()
#         test_user = User("WhatsApp password","Bihawa Mohamed","65432*")
#         test_user.save_user()
        
#         user_exists = User.user_exists("WhatsApp password")
        
#         self.assertTrue(user_exists)   
        
        
#     def test_display_all_users(self):
#         """
#         returns a list of all users saved
#         """
        
#         self.assertEqual(User.display_users(),User.user_list)
        
        
#     def text_copy_password(self):
#         """
#         Test to confirm that we are copying the password from a found detail
#         """
        
#         self.new_user.save_user()
#         User.copy_password("pass1234#")
        
#         self.assertEqual(self.new_user.password,pyperclip.paste)    
        
# if __name__ == '__main__':
#     unittest.main()
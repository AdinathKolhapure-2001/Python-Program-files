# Classes and objects
"""
class User:
    pass

user1 = User() # user1 is called an instance or object of class User

user1.first_name = "John" # data related to the object is called as field
user1.last_name = "Doe"

print(user1.first_name)

print(user1.last_name)

user2 = User()

user2.first_name = "Tony" 
user2.last_name = "Stark"

print(user2.first_name)

print(user2.last_name)


user1.age = 37
user2.favorite_book = "Harry Potter"

print(user1.age)
print(user2.favorite_book)
"""

from datetime import date

class User:
    """A member of FriendFace. For now we are only
    storing their name and birthday.
    But soon we will store an other info as well"""
    
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last names
        name_pieces = self.name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Returns the age of the user in years"""
        days_in_years = 365.2425
        return int((date.today() - self.birthday).days / days_in_years)

user = User("Tony Stark", date(1980,4,15))
print(user.name)
print(user.birthday)
print(user.first_name)
print(user.last_name)
help(User)
print(dir())
print(User.__doc__)
print(user.age())
help(user.age)

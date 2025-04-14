class User:
    
    def __init__(self, id, name):
        
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        
    def user_info(self, registration_date):
        print(f"Name:{self.name}, id: {self.id}, registration date: {registration_date}")

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    
user_1 = User("hehe", 654654)
user_2 = User("izmyname", 6574476)


user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)


print(user_2.followers)
print(user_2.following)

# user_2.user_info("01.05.2013")
# user_2.user_info("21.09.2022")

# print(user_1.followers)
# user_1.follow()
# print(user_1.followers)
# user_1.follow()
# print(user_1.followers)

# class Car:
    
#     def __init__(self, color, model, seats):
#         self.color = color
#         self.model = model
#         self.seats = seats
        
#     def race_mode(self):
#         self.seats = 2
        
        
# my_car = Car("red", "mazda", 5)
# print(my_car)
# print(my_car.seats)

# my_car.race_mode()
# print(my_car.seat
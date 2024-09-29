# # del 
# class student:
#     name='rahul'
#     def __init__(self,age):
#         self.age = age
#         # print(self.age)

    
# s1 = student(15)
# print(s1.name)
# print(s1.age)
# del s1
# print(s1.age)


# class account:
#     def __init__(self, account_no,account_pass):
#         self.account_no = account_no
#         self.__account_pass = account_pass

# user = account(12345678,543)
# print(user.account_no,"THis is your password", user.account_pass)

# Inheritance 
# class car:
#     print('parent class')
#     @staticmethod
#     def start():
#         print('parent class2')
#         print('car started....')
#         print('parent class3')

#     @staticmethod
#     def stop():
#         print('car stoped...')

# s1 = car()

# class forturner(car):
#     print('child class')
#     color = 'white'
#     sunroof = True
#     def __init__(self,type):
#         print('child class2')
#         # super().start()


# car1 = forturner('electric')

# # print(car1.color)
# print(car1.start())

# class method


# To change the classattributes 
# class person:
#     name = 'none'
#     def __init__(self,name):
#         self.__class__.name = name

# user = person('rahul')
# print(person.name)
# print(user.name)

# class method 
# class person:
#     name = 'none'
#     # def __init__(self,name):
#     #     self.__class__.name = name
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# user = person()

# user.changeName('Rahul Nagaura')
# print(person.name)
# print(user.name)

# Property 

# REPL --> Read Evaluate Print Loop 



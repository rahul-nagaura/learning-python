# # class 
# class student:
#     name= 'Rahul Nagaura'

# # object 
# s1 = student()
# print(s1.name)


# constructor 
# if do not create a constructor python automatically create a constructor 


class Student:
    def __init__(self,name):
        self.name = name
        print('adding new values')


s1 = Student('rahul')

print(s1.name)


# Normal arguments with default keyword argument.
# def foo(a=1, b=2):
#     """
#     Add a and b.
#     """
#     print(a + b)

# foo()
# # YOu can change the keyword arguments when calling the function
# foo(a=2, b=3)

# Create function to add unlimited positional arguemtns.
# Because its a tuple, you can use slicing.
# def add(*args):
#     """
#     Add all args together with a for loop.
#     """
#     total_num = 0
#     for num in args:
#         total_num += num
#     print(total_num)

# add(1, 1, 7, 8, 11)

# kwargs is multiple keyword arguments. It saves all arguments in a dictionary where you can call each by its key
# def calculate(a, b, **kwargs):
#     # print(kwargs)
#     # print(kwargs['add'])
#     # for key, value in kwargs.items():
#     #     print(f'{key}: {value}')
#     a += kwargs['add']
#     b *= kwargs['multiply']
#     print(a, b)


# calculate(a=3, b=5, add=5, multiply=2)

# Create your own kwargs class which workks the same.

# class Car:

#     def __init__(self, **kwargs):
#         self.make = kwargs['make']
#         self.model = kwargs['model']


# my_car = Car(make='Nissan', model='GT-R')
# print(my_car.model)
# But if you don't pass in a model you will get an error because it can't find it.
# You can use the model called .get which will return none if it cant find a keyword argument.

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.year = kwargs.get('year')


my_car = Car(make='Nissan')
print(my_car.model)

# Technivcally, kwargs are optional.Check documentation on all modules
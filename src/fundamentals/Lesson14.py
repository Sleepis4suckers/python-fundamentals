""" Lesson 14 - Modules, imports and packages """
# import happy
# print(happy.express())

from math import pi
# sqrt is the alias of isqrt
from math import isqrt as sqrt
# import call using from
from Lesson12more import Dog
from pixel import Pixel


def get_radius(circumference: float):
    total = (circumference / pi) / 2
    return total


def square_root(num: int):
    if num > 0:
        value = sqrt(num)
        print(value)


def dog_import():
    my_dog = Dog('Penny')
    print(my_dog.info())
    print(my_dog.make_sound())


def pixel_import():
    my_pixel = Pixel()
    print(my_pixel.screen_size)
    print(my_pixel.as_type)
    print(my_pixel.make_call())



if __name__ == '__main__':
    # print(get_radius(18.84))
    # square_root(35)
    # dog_import()
    pixel_import()


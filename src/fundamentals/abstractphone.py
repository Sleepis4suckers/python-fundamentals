""" This abstract class is the base class for subclasses """
from abc import ABC
from abc import abstractmethod


class AbstractPhone(ABC):
    @property
    @abstractmethod
    def screen_size(self):
        pass

    @property
    @abstractmethod
    def as_type(self):
        pass

    @property
    def has_print_scanner(self):
        """ A normal property within an abstract class """
        return True

    def make_call(self):
        """ This is a concrete method, which is a normal method """
        print(f'Phone unlocked using scanner {self.has_print_scanner}')
        print('Numbers dialed and call is made')
        

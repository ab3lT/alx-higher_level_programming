#!/usr/bin/python3
""" check type object"""

"""Only sub class of.
Author: Abel

"""


def inherits_from(obj, a_class):
    """ check type object"""
    """A function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class;
    otherwise False.

    Args:
        obj(any): object of the class
        a_class(type): describes the class

    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
import functools


def singleton(cls):
    """Singleton Decorator"""
    instances = dict()

    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class Dog:
    def __init__(self, *, name):
        self.name = name


dog1 = Dog(name='Fritz')
dog2 = Dog(name='Marley')

dog1.name == dog2.name

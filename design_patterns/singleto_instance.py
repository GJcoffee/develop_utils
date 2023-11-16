import sys


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    def __init__(self):
        self.value = None


@singleton
class CreateInstance:
    instance = ''

    def __init__(self):
        self.instance.value = None




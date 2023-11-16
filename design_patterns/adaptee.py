from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def request(self):
        pass


class Adaptee:
    @staticmethod
    def specific_request():
        return "Adaptee's specific requesst"


class Adapter(Target):
    def __init__(self, adaptee):
        self.apaptee = adaptee

    def request(self):
        print(f'Adapter: {self.apaptee.specific_request()}')


adapter = Adapter(Adaptee)
adapter.request()

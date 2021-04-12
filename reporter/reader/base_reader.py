from abc import ABCMeta, abstractmethod

class BaseReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def get_data(self):
        pass
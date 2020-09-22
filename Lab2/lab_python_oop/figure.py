from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def square(self):
        pass

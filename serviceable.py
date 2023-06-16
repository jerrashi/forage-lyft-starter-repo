from abc import ABC, abstractmethod

# Serviceable class is an abstract base class or a blueprint for all other classes in our program.
# Cars, which inherit from Serviceable, must have a needs_service method.
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
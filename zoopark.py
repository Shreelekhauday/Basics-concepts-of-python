from abc import ABC, abstractmethod
class abstractpets(ABC):
    def __init__(self,color,num_types,sound):
        self.color=color
        self.num_types=num_types
        self.sound=sound
@abstractmethod        
def display_details(self):
    pass


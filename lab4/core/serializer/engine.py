from abc import ABC
from abc import abstractmethod

class Engine(ABC):
    def __init__(self, path) -> None:
        super().__init__()
        self._path = path

    @abstractmethod
    def load(self) -> dict:
        pass
    
    @abstractmethod
    def dump(self, data: dict) -> None:
        pass
        

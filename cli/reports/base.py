from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self) -> list[dict[str, str]]:
        pass    

#good idea: using interfaces to define behavior without forcing implementation on subclasses

from abc import ABC, abstractmethod

class printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class scanner(printer):
    @abstractmethod
    def scan(self, document):
        pass
class fax(printer):
    @abstractmethod
    def fax(self, document):
        pass

class multifunctionmachine(printer, scanner, fax):
    def print(self, document):
        pass
    def scan(self,document):
        pass
    def fax(self,document):
        pass
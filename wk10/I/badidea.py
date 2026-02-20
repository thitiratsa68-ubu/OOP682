#bad idea: violating Open/Closed Principle by using type checking to determine behavior of function

class machine:
    def print(self, document):
        pass
    def scan(self,document):
        pass
    def fax(self,document):
        pass

class oldprinter(machine):
    def print(self, document):
        pass
    def scan(self,document):
        raise NotImplementedError("This printer cannot scan")
    def fax(self,document):
        raise NotImplementedError("This printer cannot fax")
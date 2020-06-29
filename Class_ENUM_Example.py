from enum import Enum

class Router:
    def __init__(self):
        self.Type = ""
        self.Ip = ""
        self.Interfaces = []
        super().__init__()
    
    def to_string(self):
        interface_string = ""
        for interface in self.Interfaces:
            interface_string += str(interface)
            interface_string += " "
        return self.Type + " " + self.Ip + " " + interface_string


class Interfaces(Enum):
    G00 = 1
    G01 = 2
    G02 = 3

r = Router()
r.Type = "Convergence"
r.Ip = "192.168.1.1"
r.Interfaces.append(Interfaces.G00)
r.Interfaces.append(Interfaces.G01)
print(r.to_string())

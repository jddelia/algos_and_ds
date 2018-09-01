#! /usr/bin/python3

""" This program creates common logic gates (AND, OR, NOT)
    using classes. """

class LogicGate:

    # Class is initialized with a name, and n-inputs (1 or 2).
    def __init__(self, name, ninputs, input1, input2=0):
        self.name = name.upper()
        self.ninputs = ninputs
        self.input1 = input1
        self.input2 = input2
        self.output = None
        self.logic()

    # Returns name of gate.
    def __str__(self):
        return ("Name: " + self.name)

    # This function performs gate logic for AND, OR, and NOT gates.
    def logic(self):
        if self.ninputs == 1:
            if self.input1 == 1:
                self.output = 0
            else:
                self.output = 1
        if self.ninputs == 2:
            if self.name == 'AND':
                if self.input1 == 1 and self.input2 == 1:
                    self.output = 1
                else:
                    self.output = 0
            if self.name == 'OR':
                if self.input1 == 0 and self.input2 == 0:
                    self.output = 0
                else:
                    self.output = 1

class Circuit:
    """ This class allows for circuit to be built. It initializes
        with a gate as the first component. """

    counter = 1
    def __init__(self, name, ninputs, input1, input2=0):
        self.map = []
        gate = LogicGate(name, ninputs, input1, input2)
        self.name = "Circuit " + str(Circuit.counter) + ": " + gate.name
        self.output = gate.output
        Circuit.counter += 1

    # Returns string with output of circuit.
    def __str__(self):
        return "Circuit output: " + str(self.output)

    """ Inner class, which creates a connector to connect
        gates with each other. initializes with output
        from a gate as input. Creates a link
        attribute to show diagram of connection"""
    class Connector:
        def __init__(self, other):
            self.output = other.output
            self.link = [other.name]

        # Returns string showing diagram of connection
        def __str__(self):
            if len(self.link) == 1:
                return self.link[0]
            if len(self.link) == 2:
                return self.link[0] + '-' + self.link[1]

    # Function which connects two pins/gates.
    def connect(self, other, input):
        cnnector = self.Connector(self)
        cnnector.link.append(other.name)
        if input == 1:
            other.input1 = cnnector.output
        if input == 2:
            other.input2 = cnnector.output
        other.logic()
        self.output = other.output
        self.map.append([cnnector])


g1 = LogicGate('OR', 2, 1, 0)
print(g1)
print(g1.output)

c1 = Circuit(g1.name, g1.ninputs, g1.input1, g1.input2)
g2 = LogicGate('AND', 2, 0, 1)
c1.connect(g2, 1)

print(c1.map[0][0])
print(c1)

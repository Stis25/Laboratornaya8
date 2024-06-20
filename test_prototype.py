import copy

class Prototype:
    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        return f"Name: {self.name}, Data: {self.data}"

def test_shallow_clone():
    original = ConcretePrototype("Original", [1, 2, 3])
    clone = original.clone()

    assert original.name == clone.name
    assert original.data == clone.data
    assert original.data is clone.data  

def test_deep_clone():
    original = ConcretePrototype("Original", [1, 2, 3])
    deep_clone = original.deep_clone()

    assert original.name == deep_clone.name
    assert original.data == deep_clone.data
    assert original.data is not deep_clone.data  

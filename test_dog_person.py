from lib.dog import Dog
from lib.person import Person

def test_dog_name():
    d = Dog(name="Buddy", breed="Beagle")
    assert d.name == "Buddy"
    assert d.breed == "Beagle"

def test_person_name():
    p = Person(name="john doe", job="Sales")
    assert p.name == "John Doe"
    assert p.job == "Sales"

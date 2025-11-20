from lib.dog import Dog
from lib.person import Person

def test_dog_name():
    dog = Dog(name="Rex")
    assert dog.name == "Rex"

def test_person_name():
    person = Person(name="alice")
    assert person.name == "Alice"  # title case

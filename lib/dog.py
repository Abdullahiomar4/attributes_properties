class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Fido", breed="Pug"):
        self.name = name
        self.breed = breed

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str) and 1 <= len(new_value) <= 25:
            self._name = new_value.title()
        else:
            print(f"Invalid name '{new_value}': Name must be a string between 1 and 25 characters.")

    # breed property
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_value):
        if new_value in self.approved_breeds:
            self._breed = new_value
        else:
            print(f"Invalid breed '{new_value}': Breed must be in list of approved breeds.")

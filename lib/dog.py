class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, dog_name="Fido", dog_breed="Pug"):
        self.dog_name = dog_name
        self.dog_breed = dog_breed

    # dog_name property
    @property
    def dog_name(self):
        return self._dog_name

    @dog_name.setter
    def dog_name(self, new_value):
        if isinstance(new_value, str) and 1 <= len(new_value) <= 25:
            self._dog_name = new_value.title()
        else:
            print(f"Invalid name '{new_value}': Name must be a string between 1 and 25 characters.")

    # dog_breed property
    @property
    def dog_breed(self):
        return self._dog_breed

    @dog_breed.setter
    def dog_breed(self, new_value):
        if new_value in self.approved_breeds:
            self._dog_breed = new_value
        else:
            print(f"Invalid breed '{new_value}': Breed must be in list of approved breeds.")

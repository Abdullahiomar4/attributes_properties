class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production", 
        "Legal", "Finance", "Sales", "General Management", 
        "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="John Doe", job="Sales"):
        self.name = name
        self.job = job

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

    # job property
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, new_value):
        if new_value in self.approved_jobs:
            self._job = new_value
        else:
            print(f"Invalid job '{new_value}': Job must be in list of approved jobs.")

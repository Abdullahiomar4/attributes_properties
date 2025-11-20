class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance",
        "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, person_name="John Doe", person_job="Sales"):
        self.person_name = person_name
        self.person_job = person_job

    # person_name property
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, new_value):
        if isinstance(new_value, str) and 1 <= len(new_value) <= 25:
            self._person_name = new_value.title()
        else:
            print(f"Invalid name '{new_value}': Name must be a string between 1 and 25 characters.")

    # person_job property
    @property
    def person_job(self):
        return self._person_job

    @person_job.setter
    def person_job(self, new_value):
        if new_value in self.approved_jobs:
            self._person_job = new_value
        else:
            print(f"Invalid job '{new_value}': Job must be in list of approved jobs.")

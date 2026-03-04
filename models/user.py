from models.person import Person

class User(Person):
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__(name, email)
        self._id = user_id
        self._projects = []

    @property
    def id(self):
        return self._id

    @property
    def projects(self):
        return self._projects

    def add_project(self, project):
        if project not in self._projects:
            self._projects.append(project)

    def __str__(self):
        return f"User[ID:{self._id}] - {super().__str__()}"
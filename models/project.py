from models.task import Task

class Project:
    def __init__(self, project_id: str, title: str, description: str, due_date: str, owner_id: str):
        self._id = project_id
        self._title = title
        self._description = description
        self._due_date = due_date
        self._owner_id = owner_id
        self._tasks = []

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def tasks(self):
        return self._tasks

    def add_task(self, task: Task):
        if task not in self._tasks:
            self._tasks.append(task)

    def get_task_by_id(self, task_id: str) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def __str__(self):
        return f"Project[ID:{self._id}] - {self._title} (Due: {self._due_date})"
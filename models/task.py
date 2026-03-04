class Task:
    def __init__(self, task_id: str, title: str, status: str = "Pending", assignees: list = None):
        self._id = task_id
        self._title = title
        self._status = status
        self._assignees = assignees if assignees else []

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    @property
    def assignees(self):
        return self._assignees

    def mark_complete(self):
        self._status = "Completed"

    def add_assignee(self, user_id: str):
        if user_id not in self._assignees:
            self._assignees.append(user_id)

    def __str__(self):
        return f"Task[ID:{self._id}] - {self._title} [{self._status}]"
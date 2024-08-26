# TODO: Add code here
class Todo:

    def __init__(self, code_id: int, tittle: str, description: str):
        self.code_id: int = code_id
        self.title: str = tittle
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:
    todos: dict

    def __init__(self):
        self.todos: dict = {}

    def add_todo(self, tittle: str, description: str) -> int:
        _id = len(self.todos) + 1
        market_list = Todo(_id, tittle, description)
        self.todos[_id] = market_list
        return _id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict:
        tags_counts = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tags_counts:
                    tags_counts[tag] += 1
                else:
                    tags_counts[tag] = 1
        return tags_counts

from dao.todos_dao import TodoDao


class TodoCrud:

    def get_all_todos(self):
        todo_dao = TodoDao()
        results = todo_dao.get_all_todos_dao()
        return results

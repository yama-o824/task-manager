class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._bind_events()

    def _bind_events(self):
        self.view.add_button['command'] = self.add_task
        self.view.delete_button['command'] = self.delete_task

    def add_task(self):
        task = self.view.get_task_input()
        if self.model.add_task(task):
            self.view.clear_task_input()
            self.view.update_task_list(self.model.tasks)

    def delete_task(self):
        selection = self.view.task_listbox.curselection()
        if selection:
            if self.model.delete_task(selection[0]):
                self.view.update_task_list(self.model.tasks)

class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._bind_events()

    def _bind_events(self):
        self.view.add_button['command'] = self.add_task
        self.view.delete_button['command'] = self.delete_task
        self.view.task_listbox.bind('<Double-Button-1>', self.start_edit_task)

    def add_task(self):
        task_input = self.view.get_task_input()
        if self.model.add_task(task_input['content'], task_input['due_date']):
            self.view.clear_task_input()
            self.view.update_task_list(self.model.tasks)

    def delete_task(self):
        selection = self.view.task_listbox.curselection()
        if selection:
            if self.model.delete_task(selection[0]):
                self.view.update_task_list(self.model.tasks)

    def start_edit_task(self, event=None):
        selection = self.view.task_listbox.curselection()
        if selection:
            index = selection[0]
            current_task = self.model.tasks[index]
            self.view.create_edit_window(
                current_task,
                lambda new_task: self.save_edited_task(index, new_task)
            )

    def save_edited_task(self, index, new_task):
        if self.model.edit_task(index, new_task):
            self.view.update_task_list(self.model.tasks)

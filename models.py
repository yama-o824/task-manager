import csv

class TaskModel:
    def __init__(self, file_config):
        self.file_config = file_config
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open(self.file_config['NAME'], "r", encoding=self.file_config['ENCODING']) as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        tasks.append(row[0])
        except FileNotFoundError:
            pass
        return tasks

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            self._save_tasks()
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self._save_tasks()
            return True
        return False

    def edit_task(self, index, new_task):
        if 0 <= index < len(self.tasks) and new_task:
            self.tasks[index] = new_task
            self._save_tasks()
            return True
        return False

    def _save_tasks(self):
        with open(self.file_config['NAME'], "w", encoding=self.file_config['ENCODING']) as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task])

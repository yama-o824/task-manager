import csv
from datetime import datetime, date

class Task:
    def __init__(self, content, due_date=None):
        self.content = content
        self.due_date = due_date  # datetime.date型または None

    def to_csv_row(self, config):
        due_date_str = self.due_date.strftime(config.DATE['CSV_FORMAT']) if self.due_date else ''
        return [self.content, due_date_str]

    @classmethod
    def from_csv_row(cls, row, config):
        content = row[0]
        due_date = datetime.strptime(row[1], config.DATE['CSV_FORMAT']).date() if row[1] else None
        return cls(content, due_date)

class TaskModel:
    def __init__(self, config):
        self.config = config
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open(self.config.FILE['NAME'], "r", encoding=self.config.FILE['ENCODING']) as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # 空行を無視
                        tasks.append(Task.from_csv_row(row, self.config))
        except FileNotFoundError:
            pass
        return tasks

    def add_task(self, content, due_date=None):
        if content:
            task = Task(content, due_date)
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
            self.tasks[index] = Task(new_task, self.tasks[index].due_date)
            self._save_tasks()
            return True
        return False

    def _save_tasks(self):
        with open(self.config.FILE['NAME'], "w", encoding=self.config.FILE['ENCODING']) as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow(task.to_csv_row(self.config))

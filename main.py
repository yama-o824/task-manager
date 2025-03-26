import tkinter as tk
import csv

class TaskWindow:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300
    TITLE = "タスク管理アプリ"
    LIST_WIDTH = 50
    LIST_HEIGHT = 10
    PADY = 20

    def __init__(self, root):
        self.root = root
        self.root.title(self.TITLE)

        # ウィンドウサイズと位置を設定
        self.x = (self.root.winfo_screenwidth() - self.WINDOW_WIDTH) // 2
        self.y = (self.root.winfo_screenheight() - self.WINDOW_HEIGHT) // 2
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{self.x}+{self.y}")

        # Listbox（タスクリスト）
        self.task_listbox = tk.Listbox(self.root, width=self.LIST_WIDTH, height=self.LIST_HEIGHT)
        self.task_listbox.pack(pady=self.PADY)

    def run(self):
        # タスクをリストに表示
        tasks = self.load_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

        self.root.mainloop()

    # CSVファイルからタスクを読み込む関数
    def load_tasks(self):
        tasks = []
        try:
            with open("tasks.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # 空行を無視
                        tasks.append(row[0])
        except FileNotFoundError:
            pass  # ファイルがない場合は何もしない
        return tasks

root = tk.Tk()
window = TaskWindow(root)
window.run()

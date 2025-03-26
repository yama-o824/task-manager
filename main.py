import tkinter as tk
import csv

class TaskWindow:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300
    TITLE = "タスク管理アプリ"
    LIST_WIDTH = 50
    LIST_HEIGHT = 10
    LIST_PAD_Y = 20
    TASK_ENTRY_WIDTH = 35
    ADD_BUTTON_TEXT = "追加"
    INPUT_FRAME_PAD_Y = 10
    TASK_ENTRY_PAD_X = 5
    CSV_FILE_NAME = "tasks.csv"
    CSV_FILE_ENCODING = "utf-8"
    def __init__(self, root):
        self.root = root
        self.root.title(self.TITLE)

        # ウィンドウサイズと位置を設定
        self.x = (self.root.winfo_screenwidth() - self.WINDOW_WIDTH) // 2
        self.y = (self.root.winfo_screenheight() - self.WINDOW_HEIGHT) // 2
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{self.x}+{self.y}")

        # 入力フレームの作成
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=self.INPUT_FRAME_PAD_Y)

        # タスク入力欄
        self.task_entry = tk.Entry(self.input_frame, width=self.TASK_ENTRY_WIDTH)
        self.task_entry.pack(side=tk.LEFT, padx=self.TASK_ENTRY_PAD_X)

        # 追加ボタン
        self.add_button = tk.Button(self.input_frame, text=self.ADD_BUTTON_TEXT, command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Listbox（タスクリスト）
        self.task_listbox = tk.Listbox(self.root, width=self.LIST_WIDTH, height=self.LIST_HEIGHT)
        self.task_listbox.pack(pady=self.LIST_PAD_Y)

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
            with open(self.CSV_FILE_NAME, "r", encoding=self.CSV_FILE_ENCODING) as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # 空行を無視
                        tasks.append(row[0])
        except FileNotFoundError:
            pass  # ファイルがない場合は何もしない
        return tasks
    
    # タスクを追加する関数
    def add_task(self):
        task = self.task_entry.get()
        if task:  # 空でない場合のみ追加
            # リストボックスに追加
            self.task_listbox.insert(tk.END, task)
            # CSVファイルに保存
            with open(self.CSV_FILE_NAME, "a", encoding=self.CSV_FILE_ENCODING) as file:
                writer = csv.writer(file)
                writer.writerow([task])
            # 入力欄をクリア
            self.task_entry.delete(0, tk.END)

root = tk.Tk()
window = TaskWindow(root)
window.run()

import tkinter as tk
import csv

class TaskWindowConfig:
    # ウィンドウ設定
    WINDOW = {
        'WIDTH': 450,
        'HEIGHT': 300,
        'TITLE': "タスク管理アプリ"
    }
    
    # リスト設定
    LIST = {
        'WIDTH': 50,
        'HEIGHT': 10,
        'PAD_Y': 20
    }
    
    # 入力関連設定
    INPUT = {
        'ENTRY_WIDTH': 30,
        'ADD_BUTTON_TEXT': "追加",
        'DELETE_BUTTON_TEXT': "削除",
        'FRAME_PAD_Y': 10,
        'ENTRY_PAD_X': 5,
        'BUTTON_PAD_X': 5
    }
    
    # ファイル関連設定
    FILE = {
        'NAME': "tasks.csv",
        'ENCODING': "utf-8"
    }

class TaskWindow:
    def __init__(self, root):
        self.config = TaskWindowConfig()
        self.root = root
        self._setup_window()
        self._setup_input_frame()
        self._setup_task_list()
    
    def _setup_window(self):
        self.root.title(self.config.WINDOW['TITLE'])
        x = (self.root.winfo_screenwidth() - self.config.WINDOW['WIDTH']) // 2
        y = (self.root.winfo_screenheight() - self.config.WINDOW['HEIGHT']) // 2
        self.root.geometry(f"{self.config.WINDOW['WIDTH']}x{self.config.WINDOW['HEIGHT']}+{x}+{y}")
    
    def _setup_input_frame(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=self.config.INPUT['FRAME_PAD_Y'])
        
        self.task_entry = tk.Entry(self.input_frame, width=self.config.INPUT['ENTRY_WIDTH'])
        self.task_entry.pack(side=tk.LEFT, padx=self.config.INPUT['ENTRY_PAD_X'])
        
        button_frame = tk.Frame(self.input_frame)
        button_frame.pack(side=tk.LEFT)
        
        self.add_button = tk.Button(
            button_frame,
            text=self.config.INPUT['ADD_BUTTON_TEXT'],
            command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT, padx=self.config.INPUT['BUTTON_PAD_X'])
        
        self.delete_button = tk.Button(
            button_frame,
            text=self.config.INPUT['DELETE_BUTTON_TEXT'],
            command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT, padx=self.config.INPUT['BUTTON_PAD_X'])
    
    def _setup_task_list(self):
        self.task_listbox = tk.Listbox(
            self.root, 
            width=self.config.LIST['WIDTH'], 
            height=self.config.LIST['HEIGHT']
        )
        self.task_listbox.pack(pady=self.config.LIST['PAD_Y'])

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
            with open(self.config.FILE['NAME'], "r", encoding=self.config.FILE['ENCODING']) as file:
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
            with open(self.config.FILE['NAME'], "a", encoding=self.config.FILE['ENCODING']) as file:
                writer = csv.writer(file)
                writer.writerow([task])
            # 入力欄をクリア
            self.task_entry.delete(0, tk.END)

    # タスクを削除する関数
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            return  # 選択されていない場合は何もしない
        
        # リストボックスから削除
        self.task_listbox.delete(selection[0])
        
        # CSVファイルを更新（全タスクを書き直し）
        tasks = []
        for i in range(self.task_listbox.size()):
            tasks.append(self.task_listbox.get(i))
        
        with open(self.config.FILE['NAME'], "w", encoding=self.config.FILE['ENCODING']) as file:
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow([task])

root = tk.Tk()
window = TaskWindow(root)
window.run()

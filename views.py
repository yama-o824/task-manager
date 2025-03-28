import tkinter as tk
from tkcalendar import DateEntry
from datetime import date

class TaskView:
    def __init__(self, master, config):
        self.master = master
        self.config = config
        self._setup_ui()
        self.edit_window = None  # 編集ウィンドウの参照を保持

    def _setup_ui(self):
        self._setup_window()
        self._setup_input_frame()
        self._setup_task_list()

    def _setup_window(self):
        self.master.title(self.config.WINDOW['TITLE'])
        x = (self.master.winfo_screenwidth() - self.config.WINDOW['WIDTH']) // 2
        y = (self.master.winfo_screenheight() - self.config.WINDOW['HEIGHT']) // 2
        self.master.geometry(f"{self.config.WINDOW['WIDTH']}x{self.config.WINDOW['HEIGHT']}+{x}+{y}")

    def _setup_input_frame(self):
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=self.config.INPUT['FRAME_PAD_Y'])
        
        # タスク入力欄
        self.task_entry = tk.Entry(self.input_frame, width=self.config.INPUT['ENTRY_WIDTH'])
        self.task_entry.pack(side=tk.LEFT, padx=self.config.INPUT['ENTRY_PAD_X'])
        
        # 期限ラベル
        due_date_label = tk.Label(
            self.input_frame, 
            text=self.config.DATE['LABEL_TEXT']
        )
        due_date_label.pack(side=tk.LEFT, padx=self.config.DATE['PAD_X'])
        
        # 期限設定用のDateEntry
        self.due_date_entry = DateEntry(
            self.input_frame,
            width=self.config.DATE['ENTRY_WIDTH'],
            background=self.config.DATE['BACKGROUND'],
            foreground=self.config.DATE['FOREGROUND'],
            borderwidth=self.config.DATE['BORDER_WIDTH'],
            locale=self.config.DATE['LOCALE'],
            date_pattern=self.config.DATE['DATE_PATTERN']
        )
        self.due_date_entry.pack(side=tk.LEFT, padx=self.config.DATE['PAD_X'])
        
        # ボタンフレーム
        button_frame = tk.Frame(self.input_frame)
        button_frame.pack(side=tk.LEFT)
        
        # 追加ボタン
        self.add_button = tk.Button(
            button_frame,
            text=self.config.INPUT['ADD_BUTTON_TEXT'],
        )
        self.add_button.pack(side=tk.LEFT, padx=self.config.INPUT['BUTTON_PAD_X'])
        
        # 削除ボタン
        self.delete_button = tk.Button(
            button_frame,
            text=self.config.INPUT['DELETE_BUTTON_TEXT'],
        )
        self.delete_button.pack(side=tk.LEFT, padx=self.config.INPUT['BUTTON_PAD_X'])

    def _setup_task_list(self):
        self.task_listbox = tk.Listbox(
            self.master,
            width=self.config.LIST['WIDTH'],
            height=self.config.LIST['HEIGHT']
        )
        self.task_listbox.pack(pady=self.config.LIST['PAD_Y'])

    def get_task_input(self):
        return {
            'content': self.task_entry.get(),
            'due_date': self.due_date_entry.get_date()  # DateEntryウィジェットから日付を取得
        }

    def clear_task_input(self):
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.set_date(date.today())  # 日付を今日の日付にリセット

    def update_task_list(self, tasks):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            text = task.content
            if task.due_date:
                text += f" (期限: {task.due_date.strftime(self.config.DATE['DISPLAY_FORMAT'])})"
            self.task_listbox.insert(tk.END, text)

    def create_edit_window(self, task, callback):
        if self.edit_window:
            return

        self.edit_window = tk.Toplevel(self.master)
        self.edit_window.title(self.config.EDIT['TITLE'])
        
        # ウィンドウサイズと位置を設定
        x = self.master.winfo_x() + (self.config.WINDOW['WIDTH'] - self.config.EDIT['WIDTH']) // 2
        y = self.master.winfo_y() + (self.config.WINDOW['HEIGHT'] - self.config.EDIT['HEIGHT']) // 2
        self.edit_window.geometry(f"{self.config.EDIT['WIDTH']}x{self.config.EDIT['HEIGHT']}+{x}+{y}")
        
        # 編集用のEntry
        edit_entry = tk.Entry(self.edit_window, width=self.config.EDIT['ENTRY_WIDTH'])
        edit_entry.insert(0, task)
        edit_entry.pack(pady=self.config.EDIT['ENTRY_PAD_Y'])
        edit_entry.select_range(0, tk.END)
        edit_entry.focus()
        
        # 保存ボタン
        save_button = tk.Button(
            self.edit_window,
            text=self.config.EDIT['BUTTON_TEXT'],
            command=lambda: self._save_edit(edit_entry.get(), callback)
        )
        save_button.pack(pady=self.config.EDIT['BUTTON_PAD_Y'])
        
        self.edit_window.protocol("WM_DELETE_WINDOW", self._close_edit_window)

    def _save_edit(self, new_task, callback):
        callback(new_task)  # コールバック関数を呼び出し
        self._close_edit_window()

    def _close_edit_window(self):
        if self.edit_window:
            self.edit_window.destroy()
            self.edit_window = None

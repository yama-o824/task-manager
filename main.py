import tkinter as tk
from models import TaskModel
from views import TaskView
from controllers import TaskController

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
    
    # 日付関連設定
    DATE = {
        'ENTRY_WIDTH': 12,
        'BACKGROUND': 'darkblue',
        'FOREGROUND': 'white',
        'BORDER_WIDTH': 2,
        'LOCALE': 'ja_JP',
        'DATE_PATTERN': 'y-mm-dd',
        'CSV_FORMAT': '%Y-%m-%d',
        'DISPLAY_FORMAT': '%Y/%m/%d',
        'PAD_X': 5,
        'LABEL_TEXT': '期限:'
    }
    
    # 編集ウィンドウ設定
    EDIT = {
        'WIDTH': 300,
        'HEIGHT': 100,
        'TITLE': "タスクの編集",
        'ENTRY_WIDTH': 40,
        'ENTRY_PAD_Y': 10,
        'BUTTON_TEXT': "保存",
        'BUTTON_PAD_Y': 5
    }
    
    # ファイル関連設定B
    FILE = {
        'NAME': "tasks.csv",
        'ENCODING': "utf-8"
    }

def main():
    root = tk.Tk()
    config = TaskWindowConfig()
    
    model = TaskModel(config)
    view = TaskView(root, config)
    controller = TaskController(model, view)
    
    view.update_task_list(model.tasks)
    root.mainloop()

if __name__ == "__main__":
    main()
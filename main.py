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
    
    # ファイル関連設定
    FILE = {
        'NAME': "tasks.csv",
        'ENCODING': "utf-8"
    }

def main():
    root = tk.Tk()
    config = TaskWindowConfig()
    
    model = TaskModel(config.FILE)
    view = TaskView(root, config)
    controller = TaskController(model, view)
    
    view.update_task_list(model.tasks)
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
import csv

# CSVファイルからタスクを読み込む関数
def load_tasks():
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

# Tkinterのウィンドウ作成
root = tk.Tk()
root.title("タスク管理アプリ")

# ウィンドウサイズと位置を設定
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Listbox（タスクリスト）
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=20)

# タスクをリストに表示
tasks = load_tasks()
for task in tasks:
    task_listbox.insert(tk.END, task)

root.mainloop()
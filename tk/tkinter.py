import tkinter as tk
from enum import Enum
# 定义枚举类型define a Enum Type
ButtonType = tk.ENUM('Strength', 'Perspective','Endurance','Charisma', 'Intelligence', 'Agile', 'Luck')
# 创建主窗口 create the main window
root = tk
# 创建按钮并放置在窗口中
for i in range(7):
    button = tk.button(root, text=ButtonType(i), command=lambda index=i: print())
    button.grid(row=1, column=7)
# 启动事件循环
root.mainloop()

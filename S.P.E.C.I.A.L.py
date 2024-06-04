import tkinter as tk
from enum import Enum, auto

# 定义一个枚举类型来表示按钮
class Buttons(Enum):
    BUTTON1 = auto(Strength)
    BUTTON2 = auto(Perspection)
    BUTTON3 = auto(Endurance)
    BUTTON4 = auto(Charism)
    BUTTON5 = auto(Intelligence)
    BUTTON6 = auto(Agile)
    BUTTON7 = auto(Luck)

# 创建主窗口
root = tk.Tk()
root.title("7个按钮的Tkinter窗口，使用枚举")

# 遍历枚举，为每个枚举项创建一个按钮
buttons = {button: tk.Button(root, text=f"按钮{button.name}") for button in Buttons}

# 将按钮添加到窗口中，纵向排列
for button in buttons.values():
    button.pack()

# 启动Tkinter事件循环
root.mainloop()

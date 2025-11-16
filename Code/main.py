from pasteTool import PasteAssistant
from ui import Win as MainWin
from control import Controller as MainUIController

app = MainWin(MainUIController())
if __name__ == "__main__":
    paste_assistant = PasteAssistant()
    paste_assistant.set_win(app)  # 确保传递的是当前显示的窗口
    app.mainloop()

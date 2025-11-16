import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *


class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.tk_tabs_tab0 = self.__tk_tabs_tab0(self)
        self.tk_text_t101 = self.__tk_text_t101(self.tk_tabs_tab0_0)
        self.tk_label_s_l101 = self.__tk_label_s_l101(self.tk_tabs_tab0_0)
        self.tk_label_s_l102 = self.__tk_label_s_l102(self.tk_tabs_tab0_0)
        self.tk_label_s_l103 = self.__tk_label_s_l103(self.tk_tabs_tab0_0)
        self.tk_label_s_l104 = self.__tk_label_s_l104(self.tk_tabs_tab0_0)
        self.tk_label_s_l105 = self.__tk_label_s_l105(self.tk_tabs_tab0_0)
        self.tk_label_s_l106 = self.__tk_label_s_l106(self.tk_tabs_tab0_0)
        self.tk_label_s_l107 = self.__tk_label_s_l107(self.tk_tabs_tab0_0)
        self.tk_label_s_l108 = self.__tk_label_s_l108(self.tk_tabs_tab0_0)
        self.tk_progressbar_pb101 = self.__tk_progressbar_pb101(self.tk_tabs_tab0_0)
        self.tk_text_t201 = self.__tk_text_t201(self.tk_tabs_tab0_1)
        self.tk_text_t202 = self.__tk_text_t202(self.tk_tabs_tab0_1)
        self.tk_button_b201 = self.__tk_button_b201(self.tk_tabs_tab0_1)
        self.tk_button_b202 = self.__tk_button_b202(self.tk_tabs_tab0_1)
        self.tk_label_s_l201 = self.__tk_label_s_l201(self.tk_tabs_tab0_1)
        self.tk_label_s_l202 = self.__tk_label_s_l202(self.tk_tabs_tab0_1)
        self.tk_text_t301 = self.__tk_text_t301(self.tk_tabs_tab0_2)

    def __win(self):
        self.title("PasteAssistant2")
        # 设置窗口大小、居中
        width = 360
        height = 505
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def new_style(self, widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl

    def __tk_tabs_tab0(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_tab0_0 = self.__tk_frame_tab0_0(frame)
        frame.add(self.tk_tabs_tab0_0, text="粘贴工具")
        self.tk_tabs_tab0_1 = self.__tk_frame_tab0_1(frame)
        frame.add(self.tk_tabs_tab0_1, text="文本校对")
        self.tk_tabs_tab0_2 = self.__tk_frame_tab0_2(frame)
        frame.add(self.tk_tabs_tab0_2, text="使用说明")
        frame.place(x=0, y=0, width=360, height=505)
        return frame

    def __tk_frame_tab0_0(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=360, height=505)
        return frame

    def __tk_frame_tab0_1(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=360, height=505)
        return frame

    def __tk_frame_tab0_2(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=0, width=360, height=505)
        return frame

    def __tk_text_t101(self, parent):
        text = Text(parent)
        text.place(x=4, y=4, width=350, height=392)
        return text

    def __tk_label_s_l101(self, parent):
        label = Label(parent, text="按下", anchor="center", bootstyle="default")
        label.place(x=4, y=415, width=36, height=30)
        return label

    def __tk_label_s_l102(self, parent):
        label = Label(parent, text=" LCtrl + Alt + P ", anchor="center", bootstyle="danger")
        label.place(x=35, y=415, width=96, height=30)
        return label

    def __tk_label_s_l103(self, parent):
        label = Label(parent, text="开始粘贴", anchor="center", bootstyle="default")
        label.place(x=132, y=415, width=61, height=30)
        return label

    def __tk_label_s_l104(self, parent):
        label = Label(parent, text="按下", anchor="center", bootstyle="default")
        label.place(x=4, y=440, width=36, height=30)
        return label

    def __tk_label_s_l105(self, parent):
        label = Label(parent, text=" LCtrl + Alt + L ", anchor="center", bootstyle="danger")
        label.place(x=35, y=440, width=96, height=30)
        return label

    def __tk_label_s_l106(self, parent):
        label = Label(parent, text="强制停止", anchor="center", bootstyle="default")
        label.place(x=132, y=440, width=61, height=30)
        return label

    def __tk_label_s_l107(self, parent):
        label = Label(parent, text="|  请确认输入法为英文状态", anchor="center", bootstyle="default")
        label.place(x=197, y=415, width=155, height=30)
        return label

    def __tk_label_s_l108(self, parent):
        label = Label(parent, text="|  且按 Shift 可以切换中英", anchor="center", bootstyle="default")
        label.place(x=197, y=439, width=154, height=30)
        return label

    def __tk_progressbar_pb101(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL, bootstyle="default")
        progressbar.place(x=4, y=401, width=349, height=10)
        return progressbar

    def __tk_text_t201(self, parent):
        text = Text(parent)
        text.place(x=4, y=5, width=350, height=200)
        return text

    def __tk_text_t202(self, parent):
        text = Text(parent)
        text.place(x=4, y=212, width=350, height=200)
        return text

    def __tk_button_b201(self, parent):
        btn = Button(parent, text="粘贴进框", takefocus=False, bootstyle="default outline")
        btn.place(x=190, y=423, width=82, height=41)
        return btn

    def __tk_button_b202(self, parent):
        btn = Button(parent, text="校对", takefocus=False, bootstyle="default outline")
        btn.place(x=283, y=423, width=66, height=41)
        return btn

    def __tk_label_s_l201(self, parent):
        label = Label(parent, text="将原文粘贴到上框", anchor="center", bootstyle="default")
        label.place(x=4, y=416, width=101, height=30)
        return label

    def __tk_label_s_l202(self, parent):
        label = Label(parent, text="将输入粘贴到下框", anchor="center", bootstyle="default")
        label.place(x=4, y=439, width=101, height=30)
        return label

    def __tk_text_t301(self, parent):
        text = Text(parent)
        text.place(x=4, y=4, width=350, height=463)
        return text


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_b201.bind('<Button-1>', self.ctl.pasteToT201)
        self.tk_button_b202.bind('<Button-1>', self.ctl.proofread)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_s_l101), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l102), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_s_l103), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l104), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l105), font=("微软雅黑", -12, "bold"))
        sty.configure(self.new_style(self.tk_label_s_l106), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l107), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l108), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_b201), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_b202), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l201), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_s_l202), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()

import re
import time

import pyautogui
import jieba
from pypinyin import lazy_pinyin
from pynput import keyboard
import string

from ui import Win
from control import Controller  # 你需要有一个控制器类

controller = Controller()  # 创建控制器实例

full_to_half = {'。': '.', '，': ',', '；': ';', '‘': '\'', '’': '\'', '【': '[', '】': ']',
                '、': '\\', '！': '!', '￥': '$', '……': '^', '（': '(', '）': ')'}
down_to_up = {'《': ',', '？': '/', '：': ';', '“': '\'', '”': '\'', '「': '[',
              '、': '|', '!': '1', '！': '1', '<': ',', '>': '.', '?': '/',
              ':': ';', '"': '\'', '{': '[', '}': ']', '\\': '|'}

is_running = False
is_stopping = False


class PasteAssistant:
    def __init__(self):
        self.listener = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+p': self.queue_display_text,
            '<ctrl>+<alt>+l': self.stop_paste
        })
        self.listener.start()

        self.delay_period = 1
        self.win = None  # 添加一个win引用

    def set_win(self, win):
        self.win = win

    def queue_display_text(self):
        global is_running, is_stopping
        if not is_running and self.win:
            is_running = True
            is_stopping = False
            self.win.after(0, self.display_text)

    def display_text(self):
        if self.win:
            content = self.win.tk_text_t101.get("1.0", "end-1c")
            start_paste(content)

    def stop_paste(self):
        global is_running, is_stopping
        if is_running:
            is_stopping = True


def start_paste(in_s):
    global is_running, is_stopping  # 声明全局变量
    time.sleep(3)  # 阻塞两秒

    # 定义英文字符串
    englishchar = (string.ascii_lowercase +
                   string.ascii_uppercase + ' '
                                            '\n\t1234567890!@#$%^&*()_+-=[]\\;\',./{}|:"<>?`~:')

    #  判断字符串中英文
    mode = 'English' if all(char in englishchar for char in in_s) else 'Chinese'

    if mode == 'English':
        words_list = re.split(r'(\s+)', in_s)
        words = []
        for i in words_list:
            if '\n' not in i:
                words.append(i)
                words.append(' ')
            else:
                line = i.split('\n')
                for l in line:
                    words.append(l)
                    words.append('\n')
            words.pop()
        for word in words:
            print(word)
            if is_stopping:
                break
            if word == '\n':
                pyautogui.press('enter')
            elif word == ' ':
                pyautogui.write(' ')

            else:
                for c in word:
                    if is_stopping:
                        break
                    if c in string.ascii_uppercase:
                        pyautogui.press('capslock')
                        pyautogui.typewrite(c.lower())
                        pyautogui.press('capslock')
                    else:
                        pyautogui.typewrite(c)


    elif mode == 'Chinese':
        s = in_s
        put_s = ""
        lis = jieba.lcut(s)
        for i in range(len(lis)):
            new_s = "".join(lazy_pinyin(lis[i]))
            if new_s != lis[i]:
                new_s += "1の"
                put_s += 'の'
            put_s += new_s
        for c in put_s:
            if is_stopping:
                break
            if c == '\n':
                pyautogui.press('enter')
            elif c == 'の':
                pyautogui.press('shiftleft')
            elif c in '》）】}」”':
                pyautogui.press('right')
            elif c in full_to_half:
                pyautogui.press('shiftleft')
                pyautogui.typewrite(full_to_half[c])
                pyautogui.press('shiftleft')
            elif c in down_to_up:
                pyautogui.press('shiftleft')
                pyautogui.hotkey('shiftleft', down_to_up[c])
                pyautogui.press('shiftleft')
            else:
                pyautogui.write(c)
            if c in '（《【{“':
                pyautogui.press('shiftleft')
    global is_running
    is_running = False

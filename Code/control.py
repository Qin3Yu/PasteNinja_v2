from ui import WinGUI


class Controller:
    ui: WinGUI

    def __init__(self):
        pass

    def init(self, ui):
        self.ui = ui
        self.ui.tk_text_t301.insert("1.0", tk_text_t301_text)
        self.ui.tk_text_t301.config(state='disabled')

    def pasteToT201(self, evt):
        input_text = self.ui.tk_text_t101.get("1.0", "end")
        self.ui.tk_text_t201.delete("1.0", "end")
        self.ui.tk_text_t201.insert("1.0", input_text)

    def proofread(self, evt):
        """Compare contents of tk_text_t201 and tk_text_t202 and highlight differences"""
        # Get text contents
        text1_content = self.ui.tk_text_t201.get("1.0", "end").strip()
        text2_content = self.ui.tk_text_t202.get("1.0", "end").strip()

        # Clear existing tags
        self.ui.tk_text_t201.tag_remove("match", "1.0", "end")
        self.ui.tk_text_t201.tag_remove("diff", "1.0", "end")
        self.ui.tk_text_t202.tag_remove("match", "1.0", "end")
        self.ui.tk_text_t202.tag_remove("diff", "1.0", "end")

        # Split into lines
        lines1 = text1_content.split('\n')
        lines2 = text2_content.split('\n')

        # Make both lists equal in length
        max_lines = max(len(lines1), len(lines2))
        while len(lines1) < max_lines:
            lines1.append("")
        while len(lines2) < max_lines:
            lines2.append("")

        # Compare line by line
        for line_num in range(max_lines):
            line1 = lines1[line_num]
            line2 = lines2[line_num]

            max_len = max(len(line1), len(line2))

            # Compare character by character
            for char_pos in range(max_len):
                char1 = line1[char_pos] if char_pos < len(line1) else ""
                char2 = line2[char_pos] if char_pos < len(line2) else ""

                # Calculate index positions
                start_index = f"{line_num + 1}.{char_pos}"
                end_index = f"{line_num + 1}.{char_pos + 1}"

                if char1 == char2:
                    # Matching characters - light green background
                    if char1:  # Only apply if not empty
                        self.ui.tk_text_t201.tag_add("match", start_index, end_index)
                        self.ui.tk_text_t202.tag_add("match", start_index, end_index)
                else:
                    # Different characters - light red background
                    if char1:
                        self.ui.tk_text_t201.tag_add("diff", start_index, end_index)
                    if char2:
                        self.ui.tk_text_t202.tag_add("diff", start_index, end_index)

        # Configure tag colors
        self.ui.tk_text_t201.tag_config("match", background="#D5FFD5")  # Light green
        self.ui.tk_text_t201.tag_config("diff", background="#FFD5D5")  # Light red
        self.ui.tk_text_t202.tag_config("match", background="#D5FFD5")  # Light green
        self.ui.tk_text_t202.tag_config("diff", background="#FFD5D5")  # Light red


tk_text_t301_text = ''' 
 软件说明：
     本程序提供一个模拟键盘输入的粘贴方案，用于解决带有禁止粘贴检测的网站（如学习通等）的粘贴操作。
     本程序仅供学习和交流使用，禁止投入场景使用或用于违法用途。最终解释权归 QinT6o 所有。
    
    
 输入方法：
     1.将文本复制进“粘贴工具”下的文本框中。
     2.按下快捷键后等待输入完成即可。
     3.在输入过程中，可以按下快捷键强制停止。
    
    
 注意事项：
     1.程序不会因为焦点丢失而暂停运行。
     2.输入前请确保输入法处于英文输入状态。
     3.程序仅支持中英双语输入。
     4.请确保按下shift后键盘可以切换中英。
     5.中文输入因输入法差别可能有误，请检查。
    
    
     程序还提供简单的文本校对功能，用于比对中文输入的内容差别，便于用户做出修改，在标签页“文本校对”下将程序输入后的文本粘贴到下侧文本框，点击“比较”，差别内容将会特殊显示。
 
 
                               -- by GitHub.QinT6o
                    PasteAssistant_v2.[250512]
'''

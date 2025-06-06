import os
from datetime import datetime

import pyautogui

def click(x, y):
    pyautogui.click(x, y)

def screenshot():
    download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'task')
    # 如果 task 文件夹不存在，则创建它
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    file_path = os.path.join(download_path, filename)
    controller = pyautogui.screenshot()
    controller.save(file_path)
    return file_path
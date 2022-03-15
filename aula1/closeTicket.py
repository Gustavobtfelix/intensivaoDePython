import pyautogui
import time
import pyperclip

#abrir navegador
pyautogui.PAUSE = 0.6

pyautogui.click(x=3333, y=1527)
time.sleep(5)
pyautogui.click(x=5609, y=173)
for n  in range(10):
    pyautogui.hotkey('ctrl', '2')
    pyautogui.click(x=3333, y=1527)
    time.sleep(5)
    pyautogui.click(x=5609, y=173)
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'w')

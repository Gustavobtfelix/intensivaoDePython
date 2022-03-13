#https://pyautogui.readthedocs.io/en/latest/quickstart.html

import pyautogui
import time
import pyperclip

#abrir navegador
pyautogui.PAUSE = 0.6
pyautogui.press("winleft")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.alert(r"Vai começar, aperte ok e não mexa em nada")#r = não existem funções
#pyautogui.hotkey('ctrl','t')

# abrir o drive
#pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga') ou
link ="https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(3)

#tempo entre cada ação
#acessa diretorio no drive
#pyautogui.click(457, 278, clicks = 2)
pyautogui.press('down')
pyautogui.press('up')
pyautogui.press('enter')
time.sleep(3)
#faz download de relatorio
pyautogui.click(447, 318)
pyautogui.click(1724, 154)
pyautogui.click(1485, 557)
time.sleep(4.5)

#pyautogui.click(447, 318, button='right')
#time.sleep(1)
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#pyautogui.press('down')
#time.sleep(1)
#pyautogui.press('enter')

import pandas as pd

tabela = pd.read_excel(r"C://Users/guste/Downloads/Vendas - Dez.xlsx")
print(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

#enviando e-mail

pyautogui.hotkey('ctrl', 't')
link2 ="https://mail.google.com/mail/u/0/?tab=wm#inbox"
pyperclip.copy(link2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(3)
#pyautogui.PAUSE = 0.6
pyautogui.click(67, 163)
time.sleep(2)
pyautogui.write(r"gustavofelix10@gmail.com")
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy(r"Relatório de vendas")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de {quantidade:,}

Abs
LiraPython"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

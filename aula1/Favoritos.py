import pyautogui
import time
import pyperclip

#abrir navegador
pyautogui.PAUSE = 0.6
pyautogui.press("winleft")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.alert(r"Vai começar, aperte ok e não mexa em nada")
pastas = ["SegFis", "Social", "Compromissos","Design"]
favoritos = [["https://docs.google.com/spreadsheets/d/1cfn9wd1yfGIjMLSHcN8cNKQJr869_sKNIX2PALl-6pE/edit#gid=522326322",
             "https://amigo.stone.com.br/a/dashboard/default",
             "https://stone.service-now.com/nav_to.do?uri=%2Fhome.do",
             "http://10.194.208.27:3000/auth/login?redirect=%2F,"
             "https://srv-w-access/W-Access/(S(rwbdkevcm3mt2oiqbokxym5h))/Login.aspx,"
             "http://10.194.208.27:443/SegfisAccess/jsp/login.jsp",
             "https://n356.meraki.com/PASSEIO-CORPORAT/n/EN-egbbc/manage/nodes/new_list?timespan=86400"],
             ["https://stone-co.workplace.com/?medium=email&story_id=S%3A_I100019524998272%3A3074548249495590&saml_reauth=1643649586&request_id=dalnmbhikkjifinklkkldliahmlldjfgjngjgkai&login_type=1",
             "https://coletivoaprendiz.ciedseduca.org.br",
             "https://stonepayments.atlassian.net/wiki/spaces/SCTT/pages/1467580938/Trail+Seguran+a+da+Informa+o",
             "https://sites.google.com/stone.com.br/stonetech/home?authuser=0",
             "https://github.com/PHPRio/CFP",]
             
             
             
             ]
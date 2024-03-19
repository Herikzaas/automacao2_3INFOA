import pyautogui

#clica no campo usuario
pyautogui.click(880,393,duration= 0.2)
#digita a matricula no campo
pyautogui.write('2995981',interval=0.5)

#clica no campo senha
pyautogui.click(840,460,duration= 0.2)
#digita a senha no campo
pyautogui.write('11111111',interval=0.5)

#clica no botão acessar
pyautogui.click(880, 500, duration=0.2)
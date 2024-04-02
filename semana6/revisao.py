import pyautogui

#movimentar o mouse

pyautogui.moveTo(960,540,duration =.5)
pyautogui.moveRel(100,100, duration =.5)

#arrastar o mouse

pyautogui.drag(960,540, duration= .5)
pyautogui.dragRel(100,100, duration= .5)

#clicar
pyautogui.click(960,540,clicks=2,button='RIGHT')

#rolagem
pyautogui.scroll(-2)
#pra cima positivo, pra baixo negativo, cada num a + 'e um tec do mouse(rola ai pra ver)

#escrever
pyautogui.write('Ola',interval=0.3)

#pressionar tecla
pyautogui.press('enter')

#pressionar teclas simultaneas
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

#manter as teclas pressionadas
pyautogui.keyDown('a')
pyautogui.keyUp('a')
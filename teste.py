import pyautogui
import time

# Função para tirar um screenshot
def take_screenshot(filename):
    # Aguarda 5 segundos para minimizar esta janela
    time.sleep(5)

    # Tira um screenshot
    screenshot = pyautogui.screenshot()

    # Salva o screenshot
    screenshot.save(filename)

# Exemplo de uso
take_screenshot("screenshot.png")
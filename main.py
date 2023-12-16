import pytesseract
import cv2
import pyautogui
import numpy as np
import time
import tkinter as tk

def valorDeVidaEMana():
    screenshot = pyautogui.screenshot(region=(111, 111, 45, 30))

    # Converter a imagem do PIL para o formato do OpenCV
    imagem_cv = np.array(screenshot)
    imagem_cv = cv2.cvtColor(imagem_cv, cv2.COLOR_RGB2BGR)

    path = r"C:\Program Files\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = path + r'\tesseract.exe'
    
    texto = pytesseract.image_to_string(screenshot, config="tessedit_char_whitelist=0123456789")

    return texto

def converter_para_int(texto):
    # Filtrar apenas os dígitos
    apenas_digitos = ''.join([char for char in texto if char.isdigit()])

    # Converter a string resultante para um inteiro
    # Se a string estiver vazia, retorna zero (ou outra lógica conforme necessário)
    return int(apenas_digitos) if apenas_digitos else 0

def iniciar_bot(min_life, hk_life, min_mana, hk_mana):
    print(min_life)
    print(hk_life)
    print(min_mana)
    print(hk_mana)
    while True:
        time.sleep(1)
        vidaMana = valorDeVidaEMana().split('\n')
        print(vidaMana)
        if converter_para_int(vidaMana[0]) < int(min_life) :
            pyautogui.press(hk_life)
        if converter_para_int(vidaMana[1]) < int(min_mana) :
            pyautogui.press(hk_mana)


def criar_janela():
    janela = tk.Tk()
    janela.title("Configuração de Atalhos")

    # Criação das labels de cabeçalho
    label_descricao = tk.Label(janela, text="Descrição")
    label_descricao.grid(row=0, column=0, padx=10, pady=10)

    label_valor_minimo = tk.Label(janela, text="Valor Mínimo para Ativar")
    label_valor_minimo.grid(row=0, column=1, padx=10, pady=10)

    label_hotkey = tk.Label(janela, text="Hotkey")
    label_hotkey.grid(row=0, column=2, padx=10, pady=10)

    # Criação dos campos para "Curar Vida"
    label_curar_vida = tk.Label(janela, text="Curar Vida")
    label_curar_vida.grid(row=1, column=0, padx=10, pady=5)

    input_vida_min = tk.Entry(janela)
    input_vida_min.insert(0, "3700") 
    input_vida_min.grid(row=1, column=1, padx=10, pady=5)

    input_vida_hotkey = tk.Entry(janela)
    input_vida_hotkey.insert(0, "f4") 
    input_vida_hotkey.grid(row=1, column=2, padx=10, pady=5)

    # Criação dos campos para "Curar Mana"
    label_curar_mana = tk.Label(janela, text="Curar Mana")
    label_curar_mana.grid(row=2, column=0, padx=10, pady=5)

    input_mana_min = tk.Entry(janela)
    input_mana_min.insert(0, "1300") 
    input_mana_min.grid(row=2, column=1, padx=10, pady=5)

    input_mana_hotkey = tk.Entry(janela)
    input_mana_hotkey.insert(0, "f5") 
    input_mana_hotkey.grid(row=2, column=2, padx=10, pady=5)

    # Criação do botão "Iniciar"
    botao_iniciar = tk.Button(janela, text="Iniciar", command=lambda:iniciar_bot(input_vida_min.get(), input_vida_hotkey.get(), input_mana_min.get(), input_mana_hotkey.get() ))
    botao_iniciar.grid(row=3, column=0, columnspan=3, pady=10)


    janela.mainloop()

criar_janela()

# 
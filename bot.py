from pywinauto.application import Application
from pywinauto import keyboard
from getpass import getuser
from time import sleep
from PIL import Image

import pytesseract
import os

def execute_bot():
    try:
        global app
        app = Application(backend='uia').start(f"C:\\Users\\{getuser()}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        sleep(3)

        app = Application(backend='uia').connect(title_re='Telegram')
        print("\nConectado ao Telegram")

        app.TelegramDesktop.set_focus()
        
        keyboard.send_keys('Mensagens', pause=0)
        sleep(1)
        keyboard.send_keys("{ENTER}")
        print("Contato selecionado")

        sleep(2)

    except Exception as error:
        print(error)
    
    save_photo()
    ler_imagens()
    write_text()
    sleep(3)
    app.kill()

def save_photo():
    try:
        app.TelegramDesktop.GroupBox.GroupBox22.click_input(button='right', coords=(100, -100))
        sleep(2)

        app.TelegramDesktop.GroupBox.GroupBox3.click_input()
        sleep(2)

        inputlocal = app.TelegramDesktop.child_window(title="Todos os locais", control_type="SplitButton")
        inputlocal.click_input()
        sleep(1)

        keyboard.send_keys(os.path.abspath('./'), with_spaces=True, pause=0)
        sleep(1)

        keyboard.send_keys("{ENTER}")
        sleep(1)

        app.TelegramDesktop.Salvar.click_input()

        print("Imagem salva")

    except Exception as error:
        print(error)     

def write_text():
    try:
        keyboard.send_keys(pytesseract.image_to_string(Image.open(list_photos[-1]), config='--psm 6'), pause=0)
        sleep(1)
        keyboard.send_keys("{ENTER}")
        
        print("Texto enviado com sucesso")
        os.remove(list_photos[-1])

    except Exception as error:
        print(error)

def ler_imagens():
    global list_photos, file
    sleep(3)
    path = os.path.abspath('./')
    dirs = os.listdir(path)
    list_photos = []

    for file in dirs:
        if ".jpg" in file or ".png" in file:
            list_photos.append(file)

def startBot():
    execute_bot()
    while True:
        sleep(600)
        execute_bot()

startBot()

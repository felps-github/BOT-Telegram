from pywinauto.application import Application
from pywinauto import keyboard
from getpass import getuser
from time import sleep

import os

def execute_bot():
    try:
        global app
        app = Application(backend='uia').start(f"C:\\Users\\{getuser()}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        sleep(3)

        app = Application(backend='uia').connect(title_re='Telegram')
        print("Conectado ao Telegram")

        app.TelegramDesktop.set_focus()
        
        keyboard.send_keys('Mensagens')
        sleep(2)
        keyboard.send_keys("{ENTER}")
        print("Contato selecionado")

        sleep(3)

    except Exception as error:
        print(error)
    
    save_photo()
    sleep(3)
    app.kill()

def save_photo():
    try:
        app.TelegramDesktop.GroupBox.GroupBox22.click_input(button='right', coords=(100, -100))
        sleep(3)

        app.TelegramDesktop.GroupBox.GroupBox3.click_input()
        sleep(3)

        inputlocal = app.TelegramDesktop.child_window(title="Todos os locais", control_type="SplitButton")
        inputlocal.click_input()
        sleep(1)

        keyboard.send_keys(os.path.abspath('./'), with_spaces=True)
        sleep(1)

        keyboard.send_keys("{ENTER}")
        sleep(1)

        app.TelegramDesktop.Salvar.click_input()

        print("Imagem salva")
        sleep(3)

    except Exception as error:
        print(error)

execute_bot()

from pywinauto.application import Application
from pywinauto import keyboard
from getpass import getuser
from time import sleep

def acessTelegram():
    try:
        app = Application(backend='uia').start(f"C:\\Users\\{getuser()}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        sleep(2)
        app = Application(backend='uia').connect(title_re='Telegram', visible_only= True)

        app.TelegramDesktop.set_focus()

        keyboard.send_keys('Mensagens')
        sleep(2)

        keyboard.send_keys("{ENTER}")
        sleep(2)

        app.TelegramDesktop.GroupBox.GroupBox22.GroupBox.click_input()

    except Exception as error:
        print(error)

acessTelegram()
from pywinauto.application import Application
from pywinauto import keyboard
from getpass import getuser
from time import sleep

def acessTelegram():
    try:
<<<<<<< HEAD
        
=======
        app = Application(backend='uia').start(f"C:\\Users\\{getuser()}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        sleep(3)
        app = Application(backend='uia').connect(title_re='Telegram')

        app.TelegramDesktop.set_focus()

        keyboard.send_keys('Mensagens')
        sleep(2)

        keyboard.send_keys("{ENTER}")
        sleep(2)

        app.TelegramDesktop.GroupBox.GroupBox12.click_input()
        sleep(2)
        app.TelegramDesktop.GroupBox11.GroupBox2.GroupBox8.click_input()
        
        sleep(5)
        app.kill()
>>>>>>> parent of 74a6f1f (update)

    except Exception as error:
        print(error)

acessTelegram()
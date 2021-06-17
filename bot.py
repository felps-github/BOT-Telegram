from pywinauto import keyboard
from pywinauto.application import Application
from time import sleep

app = Application(backend='uia').start(r"C:\Users\felipe.oliveira\AppData\Roaming\Telegram Desktop\Telegram.exe")
sleep(2)
app = Application(backend='uia').connect(title_re='Telegram', visible_only= True)

app.TelegramDesktop.set_focus()

keyboard.send_keys('Mensagens')
sleep(2)

keyboard.send_keys("{ENTER}")
sleep(2)

app.TelegramDesktop.GroupBox.GroupBox22.GroupBox.click_input()

# profile = app.TelegramDesktop.GroupBox12
# profile.click_input()
# sleep(3)

# photos = app.TelegramDesktop.GroupBox100
# photos.click_input()
# sleep(2)

# # Menu, Minimizar, Maximizar e Fechar o Telegram
# a = app.TelegramDesktop.GroupBox21
# a.click_input()

# menu = app.TelegramDesktop.GroupBox.GroupBox2
# sleep(2)
# menu.click_input()
# fecharTelegram = app.TelegramDesktop.GroupBox24
# sleep(3)
# fecharTelegram.click_input()

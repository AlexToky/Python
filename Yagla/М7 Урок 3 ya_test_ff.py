# Variables
# 
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#
from time import sleep
#
browser = webdriver.Firefox()
browser.start_session # new window
browser.get("https://ya.ru/")
#
# $$('a[data-statlog="headline.enter"]') # поиск по тегу
# $$('a.home-link2.headline__personal-enter') # поиск по двум классам
# $$('a[href="https://passport.yandex.ru"]') # поиск по href
#
browser.find_element(By.CLASS_NAME, 'headline__personal-enter').click() #enter login page
#
sleep(3)
#
def loginByEmail(addr):
    from tkinter import messagebox
    from tkinter import simpledialog
    #
    browser.find_element(By.CSS_SELECTOR, 'button[data-type="login"]').click #option 'Login by email' is choosen
    askMe = messagebox.askyesno('Login to Ya.ru', 'Would you prefer random values for email and password?')
    if askMe:
        from faker import Faker
        fake = Faker()
        addr = fake.email()
        pwrd = fake.password()

    else:
        addr = simpledialog.askstring('Login to Ya.ru', 'Enter email address')
        pwrd = simpledialog.askstring('Login to Ya.ru', 'Enter password')

    print("email "+ addr)
    print("password " + pwrd)

    
    browser.find_element(By.CSS_SELECTOR, "#passp-field-login").send_keys(addr)
    return None #error supposed to be returned


#loginByEmail(email_addr)

sleep(3)
browser.quit

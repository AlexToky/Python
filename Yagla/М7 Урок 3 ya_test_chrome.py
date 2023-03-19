from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

browser = webdriver.Chrome()
browser.get("https://ya.ru/")

# $$('a[data-statlog="headline.enter"]') # поиск по тегу
# $$('a.home-link2.headline__personal-enter') # поиск по двум классам
# $$('a[href="https://passport.yandex.ru"]') # поиск по href

browser.find_element(By.CLASS_NAME, 'headline__personal-enter').send_keys('selenium')

sleep(10)
browser.quit

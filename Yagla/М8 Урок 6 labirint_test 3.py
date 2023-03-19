# Variables and libr
url = 'https://labirint.ru/'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from time import sleep
#
from tkinter import messagebox
from tkinter import simpledialog
#
cookie = {
    'name': 'cookie_policy',
    'value': '1'
}
#
browser = webdriver.Chrome()
# запуск в новом окне браузера
browser.start_session
browser.get(url)
browser.add_cookie(cookie)
browser.implicitly_wait(4)
#
# диалоговое окно по поисковой строке
sStr = simpledialog.askstring(url, 'Enter search string\nMinimum 3 characters length')
if sStr is None:
    # если нажата кнопка Отмена
    browser.quit()
    quit()
if len(sStr) < 3:    
    # если длина строки поиска менее 3 символов
    browser.quit()
    quit()
    #
browser.find_element(By.CSS_SELECTOR, '#search-field').send_keys(sStr)
form = browser.find_element(By.CSS_SELECTOR, '#searchform')
form.submit()
# переход на таблицу
url_list = url + "search/" + sStr + "/?stype=0&display=table"
browser.get(url_list)
# маркер наличия книг по запросу (ДА - длина массива более 0)
req_Fnd = len(browser.find_elements(By.XPATH, "//span[contains(@class,'b-stab-e-slider-item-e-txt-m-small js-search-tab-count')]"))
# массив книг по запросу на текущей странице
bList = browser.find_elements(By.CSS_SELECTOR, 'a.buy-link')
if req_Fnd < 1:
    # Если по запросу ничего не найдено, на странице есть книги, 
    # подходящие под  предложенный CSS-селектор 'a.buy-link'
    # Предлагается выйти из программы тестирования, 
    # либо использовать для покупки книги, предложенные Лабиринтом
    msg = "No items found on your request\n"+\
        sStr +"\nWould you prefer to purchase default items instead?\n"+\
            "Press YES to confirm\n"+"Press NO to quit testing"
    if not messagebox.askyesno(url, msg):
        browser.quit()
        quit()
#else:
# определение максимального числа книг для покупки = число элементов массива,
# созданного с помощью CSS-селектора 'a.buy-link'
req_OnP = len(bList)
if req_Fnd > 0:
    # преобразование в число текста числа книг в магазине
    req_Fnd = int(browser.find_element(By.XPATH, "//span[contains(@class,'b-stab-e-slider-item-e-txt-m-small js-search-tab-count')]").text)
else:
    # если результат выполнения строки запроса был неудачным
    req_Fnd = req_OnP
# информационно-диалоговое окно
# число книг, найденных по запросу
# число книг, доступных для заказа
# поле ввода требуемого числа книг для тестирования с учётом мин./ макс. количества
msg = str(req_Fnd) + " books found on your request\n" + \
    str(req_OnP) + " books are available to purchase\n" + \
        "Enter required number of books to purchase\n" + \
            "or Cancel to quit"
b_Ordered = simpledialog.askinteger(url,msg,initialvalue=1,minvalue=1,maxvalue=req_OnP)
# Если нажата кнопка Отмена
if b_Ordered is None:
    browser.quit()
    quit()
#
locator = 'table.products-table'
#
WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )
for i in range(0, b_Ordered):
    bList[i].click()
#
url_Cart = url + "cart/"
# Переход в Корзину
browser.get(url_Cart)
#
#
locator = browser.find_element(By.CSS_SELECTOR, "#ui-id-4").text
messagebox.Message(locator)
# Подготовка к очистке Корзины перед выходом
basket_Clean = browser.find_element(By.CSS_SELECTOR, 'a.b-link-popup')
#
if not basket_Clean is None:
    # Очистка корзины
    basket_Clean.click()
    sleep(10)
browser.quit()
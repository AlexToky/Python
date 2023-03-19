# Variables and libr
url = 'https://labirint.ru/'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
browser = webdriver.Firefox()
#
browser.start_session # new window
browser.get(url)
browser.add_cookie(cookie)
#sStr = "python"
#bNum = 3
sStr = simpledialog.askstring('Test of ' + url, 'Enter search string')
#bNum = simpledialog.askinteger('Test of ' + url, 'Enter number of books')
#print("Search for " + sStr)
#print(str(bNum) + " books")
#
if len(sStr) > 2:
    browser.find_element(By.CSS_SELECTOR, '#search-field').send_keys(sStr)
    form = browser.find_element(By.CSS_SELECTOR, '#searchform')
    form.submit()
    #
    #https://www.labirint.ru/search/python/?stype=0&display=table
    url_list = url + "search/" + sStr + "/?stype=0&display=table"
    #browser.find_element(By.CSS_SELECTOR, 'a[href="?stype=0&display=table"]').click()      #switch to list
    # Arr = browser.find_elements(By.CSS_SELECTOR, 'a[href="?stype=0&display=table"]')
    # print(Arr)
    browser.get(url_list)
    #
    req_Fnd = len(browser.find_elements(By.XPATH, "//span[contains(@class,'b-stab-e-slider-item-e-txt-m-small js-search-tab-count')]"))
    #if len(req_Fnd) = 0:
    #    msg = "No items found on your request\n"+sStr #+"\n"+"Would you prefer to purchase default items instead?\n"+"Press YES to confirm\n"+"Press NO to quit testing"
    #   if messagebox.askyesno(url, msg):




    bList = browser.find_elements(By.CSS_SELECTOR, 'a.buy-link')
    b_Found = browser.find_element(By.XPATH, "//span[contains(@class,'b-stab-e-slider-item-e-txt-m-small js-search-tab-count')]")
    if len(bList) > 0:
        #
        #if bNum > len(bList):
        #    bNum = len(bList)
        #for i in range(0, bNum):
        #    bList[i].click()
        #
        #    
        # browser.find_element(By.CLASS_NAME, 'a.b-header-b-personal-e-icon-count-m-cart basket-in-cart-a').click()   # doesn't work
        url_Cart = url + "/cart/"
        browser.get(url_Cart)
        sleep(5)
        browser.find_element(By.CSS_SELECTOR, 'a.basket-in-cart-a').click()

    browser.quit()
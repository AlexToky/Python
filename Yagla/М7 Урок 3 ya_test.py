from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://selenium.dev/')


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# from webdrivermanager.chrome import ChromeDriverManager
#
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().download_and_install()))
# browser.get('http://selenium.dev/')
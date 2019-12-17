import requests 
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site_url = 'http://www.amazon.co.uk'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="C:\\Users\\Vlad\\Documents\\Apps\\chromedriver_win32 for 78\\chromedriver.exe", chrome_options=options)

search_term = "addon items only"

driver.get(site_url)
element = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
element.send_keys(search_term)
element.send_keys(Keys.ENTER)

products = []

page = 1

while True:
    if page != 1:
        try:
            driver.get(driver.current_url + "&page" + str(page))
        except:
            print("exept")
            break
    for c, i in enumerate(driver.find_elements_by_class_name('s-result-item')):

        try:
            name = i.find_element_by_tag_name("h2").text
            price = float(i.find_element_by_class_name('a-price').text.replace('\n', '.').replace('£', ''))
            link = i.find_elements_by_xpath('//h2/a')[c].get_attribute("href")
            print("price", price)
        except Exception:
            break
        
    page = page + 1
    if page == 11:
        break
    # print(page)
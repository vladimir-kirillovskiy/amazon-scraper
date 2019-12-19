import requests 
import json
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from product import Product

# def unique(list1): 
  
#     # intilize a null list 
#     unique_list = [] 
      
#     # traverse for all elements 
#     for x in list1: 
#         # check if exists in unique_list or not 
#         if x not in unique_list: 
#             unique_list.append(x) 
    
#     return unique_list

site_url = 'http://www.amazon.co.uk'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="C:\\Users\\Vlad\\Documents\\Apps\\chromedriver_win32 for 78\\chromedriver.exe", chrome_options=options)

# search_term = "addon items only"
search_term = input("Search Addon:")

driver.get(site_url)
element = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
element.send_keys(search_term)
element.send_keys(Keys.ENTER)

products = []

page = 1

last_page = int(driver.find_elements_by_xpath("//ul[@class='a-pagination']/li[6]")[0].text)

while True:
    print('Page:', page)
    if page != 1:
        try:
            driver.get(driver.current_url + "&page=" + str(page))
        except:
            print("exept")
            break

    result_items = driver.find_elements_by_class_name('s-result-item')

    for c, i in enumerate(result_items):
        should_add = False
        try:
            name = i.find_element_by_tag_name("h2").text
            price = float(i.find_element_by_class_name('a-price').text.replace('\n', '.').replace('£', ''))
            link = i.find_elements_by_xpath('//h2/a')[c].get_attribute("href")
           
            # clean link
            index = link.find('ref=')
            if index >= 0:
                link = link[:index]

            try:
                if i.find_element_by_class_name('s-addon-highlight-color'):
                    should_add = True

            except Exception:
                should_add = False

        except Exception:
            print("-- Couldn't fetch price")
            # print(i.find_element_by_tag_name("h2").text)

        product = Product(name, price, link)
        if should_add:
            products.append(product)

    page = page + 1
    if page > last_page:
        break

save_name = search_term.replace(' ', '_').replace('.', '_').replace(',', '_').replace('/', '_')
# remove duplicates
print("size of product after:", len(products))

with open(save_name + '.txt', 'w') as outfile:
    for i, product in enumerate(products):
        json.dump(product.serialize(), outfile)

 
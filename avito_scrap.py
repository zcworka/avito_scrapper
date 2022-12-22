from itertools import product
from pydoc import source_synopsis
from socket import timeout
from bs4 import BeautifulSoup, Tag
import os
from requests import get
from re import search
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.common.exceptions import TimeoutException 
import re

class Product:
    def __init__(self, title, price, href):
        self.title = title
        self.price = price
        self.href = href


# two ways to get html source
def try_by_requests(source):
    html = get(source).text
    if not "Доступ ограничен: проблема с IP" in html:
        soup = BeautifulSoup(html, "html.parser")
        product_class = search(r'iva-item-list-\S*', html).group()
        all_products = [link for link in soup.find_all("div", {"class":product_class})]
        return all_products
    else: 
        return False
def try_by_selemium(source):
    try:
        driver = webdriver.Firefox(executable_path="./geckodriver")
        driver.set_page_load_timeout(10)
        html = driver.get(source)
        html = driver.page_source
        driver.close()
        
    except TimeoutException:
        html = driver.page_source
        driver.close()
        # 
    soup = BeautifulSoup(html, "html.parser")
    product_class = search(r'iva-item-list-\S*', html).group()
    all_products = [link for link in soup.find_all("div", {"class":product_class})]
    return all_products

# trying to get products's html codes by available ways
def get_all_products(source):
    all_products = try_by_requests(source)
    if not all_products: print("\n=====\nRequests is refused.\n=====\n")
    if not all_products: all_products = try_by_selemium(source)
    return all_products
    
# convert html to Product's objects
def parse_products_to_objects(products_list, avito_url):
    products_objects = []
    for div in products_list:

        title_class = search(r'title-root-\S*', str(div)).group()
        title = div.find("h3", {"class":title_class}).text

        href_class = search(r'link-link-\S*', str(div)).group()
        href = div.find("a", {"class":href_class}).get("href")
        if not avito_url in href:
            href = f"{avito_url}/{href}"

        price_class = search(r'price-text-\S*', str(div)).group()
        price = div.find("span", {"class":price_class}).text
        price = "".join(re.findall(r'\d+', price))

        products_objects.append(Product(title=title, href=href, price=price))
    return products_objects


# return most cheap product from products list
def get_most_cheap_product(products):
    most_low_price = min([product_price.price for product_price in products])
    most_cheap_product = [product for product in products if product.price == most_low_price][0]
    return most_cheap_product





    





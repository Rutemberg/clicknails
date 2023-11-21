from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(options)


driver.get("https://shopping.google.com.br/")
elem = driver.find_element(By.ID, "REsRA")
elem.click()
elem.send_keys("Esmalte Bellaoggi Rosa Millennial")
elem.send_keys(Keys.ENTER)
elem = driver.find_element(By.CLASS_NAME, "sh-pr__product-results-grid")
cards = elem.find_elements(By.CLASS_NAME, "sh-dgr__grid-result")

obj = []

for card in cards:
    valor = card.find_element(By.CLASS_NAME, "OFFNJ")
    vendedor = card.find_element(By.CLASS_NAME, "IuHnof")
    link = card.find_element(By.CLASS_NAME, "translate-content")

    obj.append({"vendedor": vendedor.text, "valor": valor.text, "link": link.get_property("href")})


print(obj)

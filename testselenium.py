from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random

marcas = [
    "Risqué",
    "Colorama",
    "Impala",
    "Hits Speciallità",
    "Dailus",
    "Vult",
    "Ana Hickmann",
    "Mohda",
    "Eliana Dote",
    "Ludurana",
    "Blant Colors",
    "DNA Italy",
    "Novo Toque",
    "Bella Brazil",
    "Beauty Color",
    "Koloss",
    "Max Beauty",
    "Top Beauty",
    "Jade",
    "Granado",
    "Jequiti",
    "Mundial Impala",
    "Passe Nati",
    "Hello Kitty",
    "Ellen Gold",
    "Realce",
    "View Cosméticos",
    "Foup",
    "B.U.",
    "Ricca",
    "Boticário",
    "Vefic",
    "Ten Beauté",
    "Luxor",
    "Haskell",
    "Panvel",
    "Preta Gil",
    "Luzzy",
    "Yenzah",
    "Alessandro",
    "Flormar",
    "Ruby Rose",
    "Mavala",
    "Kiss New York",
    "Super Pérola",
    "Latika",
    "Farmax",
    "Altamoda",
    "Tracta",
    "Kolt",
    "Lacan",
    "Alfaparf",
    "Nyce",
    "Mia Secret",
    "Cora",
    "Bellaoggi",
    "Verniz",
    "Lokenzzi",
    "Ricca",
    "Vernier",
    "Dracarys",
]
COR = [
    "Vermelho",
    "Rosa",
    "Nude",
    "Branco",
    "Preto",
    "Azul",
    "Verde",
    "Amarelo",
    "Laranja",
    "Roxo",
    "Marrom",
    "Cinza",
    "Prata",
    "Dourado",
    "Bordô",
    "Coral",
    "Turquesa",
    "Lilás",
    "Bege",
    "Rubi",
    "Taupe",
    "Pêssego",
    "Menta",
    "Ameixa",
    "Burgundy",
    "Champagne",
    "Terracota",
    "Malva",
    "Mostarda",
    "Salmão",
    "Celeste",
    "Grafite",
    "Púrpura",
    "Cobre",
    "Índigo",
    "Fúcsia",
    "Caramelo",
    "Cobalto",
    "Marsala",
    "Ocre",
    "Salmon Rose",
    "Pistache",
    "Lavanda",
    "Açaí",
    "Gelo",
    "Orquídea",
    "Rosa Millennial",
    "Verde Militar",
]


options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(options)
driver.get("https://www.google.com.br/?hl=pt-BR")
elem = driver.find_element(By.ID, "APjFqb")
elem.click()
nome = f"Esmalte {random.choice(marcas)} {random.choice(COR)}"
print("*" * 50, nome)
elem.send_keys(nome)
elem = driver.find_element(By.NAME, "btnK")
elem.click()

try:
    elem = driver.find_element(
        By.XPATH,
        "//g-inner-card/div/div/img",
    )
    src = elem.get_attribute("src")

except NoSuchElementException:
    src = ""

print(elem.get_attribute("src"))

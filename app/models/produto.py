import time
from app.extensions import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProdutoImagem:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument("--headless")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("enable-automation")
        # self.options.add_argument("--disable-infobars")
        # self.options.add_argument("--disable-dev-shm-usage")
        # self.options.add_argument("start-maximized")
        # self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # self.options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(self.options)
        
    def get_imagem(self, nome):
        self.driver.get("https://images.google.com.br")
        elem = self.driver.find_element(By.ID, "APjFqb")
        elem.click()
        elem.send_keys(nome)
        elem.send_keys(Keys.ENTER)
        try:
            nome_elem = ".isv-r:nth-child(2) .rg_i"
            elem = self.driver.find_element(
                By.CSS_SELECTOR,
                nome_elem,
            )
            src = elem.get_attribute("src")
        except NoSuchElementException:
            src = "https://cdn-icons-png.flaticon.com/512/2444/2444896.png"
        return src

    def close(self):
        return self.driver.close()


class Produto(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    codigobarra: Mapped[str] = mapped_column(String, nullable=False)
    img: Mapped[str] = mapped_column(String, nullable=False)
    marca: Mapped[str] = mapped_column(String, nullable=False)
    cor: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<Produto "{self.nome}">'

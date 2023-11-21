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
import re


class ProdutoAnalytics:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("enable-automation")
        self.options.add_argument("--disable-dev-shm-usage")
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
            src = "https://cdn-icons-png.flaticon.com/512/3163/3163203.png"
        return src

    def pesquisa_precos(self, nome):
        lista = []
        self.driver.get("https://shopping.google.com.br/")
        elem = self.driver.find_element(By.ID, "REsRA")
        elem.click()
        elem.send_keys(nome)
        elem.send_keys(Keys.ENTER)
        try:
            elem = self.driver.find_element(
                By.CLASS_NAME, "sh-pr__product-results-grid"
            )
            cards = elem.find_elements(By.CLASS_NAME, "sh-dgr__grid-result")
            for card in cards:
                valor = card.find_element(By.CLASS_NAME, "OFFNJ")
                vendedor = card.find_element(By.CLASS_NAME, "IuHnof")
                link = card.find_element(By.CLASS_NAME, "translate-content")
                nome = link.find_element(By.TAG_NAME, "h3")

                lista.append(
                    {
                        "vendedor": vendedor.text,
                        "valor_": int(re.findall("\\d+", valor.text)[0]),
                        "valor": valor.text,
                        "link": link.get_property("href"),
                        "nome": nome.text,
                    }
                )
        except:
            return lista
        return lista

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
    cor: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self):
        return f'<Produto "{self.nome}">'

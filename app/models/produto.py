from app.extensions import db
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException


class ProdutoImagem:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.options)

    def get_img(self, nome):
        self.driver.get("https://www.google.com.br/?hl=pt-BR")
        elem = self.driver.find_element(By.ID, "APjFqb")
        elem.click()
        elem.send_keys(nome)
        elem.send_keys(Keys.ENTER)
        try:
            elem = self.driver.find_element(
                By.XPATH,
                "//g-inner-card/div/div/img",
            )
            src = elem.get_attribute("src")

        except NoSuchElementException:
            elem = self.driver.find_element(
                By.XPATH,
                "/html/body/div[6]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/g-section-with-header/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div/img",
            )
            src = elem.get_attribute("src")
        else:
            src = "https://cdn-icons-png.flaticon.com/512/2444/2444896.png"
        return src


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

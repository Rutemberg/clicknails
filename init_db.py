from app.extensions import db
from app.models.produto import Produto, ProdutoImagem
from app.models.fornecedor import Fornecedor
import random
from faker import Faker
from app.constants import COR, MARCAS

db.drop_all()
db.create_all()
fake = Faker()

img = ProdutoImagem()

for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    codigobarra = random.randrange(100000000000000000000, 999999999999999999999)
    quantidade = random.randrange(1, 100)
    preco = round(random.uniform(5.00, 100.50), 2)
    marca = random.choice(MARCAS)
    cor = random.choice(COR)
    nome = f"Esmalte {marca} {cor}"
    src = img.get_img(nome)
    produto = Produto(
        nome=nome,
        quantidade=quantidade,
        preco=preco,
        codigobarra=f"{codigobarra}",
        marca=marca,
        cor=cor,
        img=src,
    )
    db.session.add(produto)
    print(produto)
    print("--")
    db.session.commit()
for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    cnpj = random.randrange(10000000000, 99999999999)
    telefone = fake.phone_number()
    fornecedor = Fornecedor(nome=f"{fake.name()}", cnpj=cnpj, telefone=telefone)
    db.session.add(fornecedor)
    print(fornecedor)
    print("--")
    db.session.commit()

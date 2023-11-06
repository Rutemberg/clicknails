from app.extensions import db
from app.models.produto import Produto
import random

db.drop_all()
db.create_all()

for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    codigobarra = random.randrange(10000000000, 99999999999)
    quantidade = random.randrange(1, 100)
    
    produto = Produto(nome=f'Produto #{random_num}',
                quantidade=quantidade, preco=10.80, codigobarra=f"{codigobarra}")
    db.session.add(produto)
    print(produto)
    print('--')
    db.session.commit()
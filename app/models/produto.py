from app.extensions import db
from sqlalchemy import Integer, String, Double
from sqlalchemy.orm import Mapped, mapped_column

class Produto(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    preco: Mapped[float] = mapped_column(Double, nullable=False)
    codigobarra: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<Produto "{self.nome}">'

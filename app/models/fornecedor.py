from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Fornecedor(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    cnpj: Mapped[str] = mapped_column(String, nullable=False)
    nome: Mapped[int] = mapped_column(String, nullable=False)
    telefone: Mapped[float] = mapped_column(String, nullable=False)

    def __repr__(self):
        return f'<Fornecedor "{self.nome}">'

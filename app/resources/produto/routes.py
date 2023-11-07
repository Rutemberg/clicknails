from flask import render_template, request, url_for, redirect
from app.resources.produto import bp
from app.extensions import db
from app.models.produto import Produto


@bp.route("/", methods=("GET", "POST"))
def index():
    produtos = Produto.query.all()

    if request.method == "POST":
        novo_produto = Produto(
            nome=request.form["nome"],
            preco=request.form["preco"],
            quantidade=request.form["quantidade"],
            codigobarra=request.form["codigobarra"],
        )
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for("produto.index"))

    return render_template("produto/index.html", produtos=produtos)

@bp.route("/<int:id>")
def delete(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for("produto.index"))
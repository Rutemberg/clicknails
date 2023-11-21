import operator
from flask import render_template, request, url_for, redirect
from app.resources.produto import bp
from app.extensions import db
from app.models.produto import Produto, ProdutoAnalytics


@bp.route("/", methods=("GET", "POST"))
def index():
    produtos = Produto.query.all()
    if request.method == "POST":
        img = ProdutoAnalytics()
        nome = request.form["nome"]
        src = img.get_imagem(nome)
        novo_produto = Produto(
            nome=request.form["nome"],
            preco=request.form["preco"],
            quantidade=request.form["quantidade"],
            codigobarra=request.form["codigobarra"],
            marca=request.form["marca"],
            cor=request.form["cor"],
            img=src,
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


@bp.route("/detalhes/<int:id>", methods=("GET", "POST"))
def alterar_produto(id):
    produto = Produto.query.get_or_404(id)
    analytics = ProdutoAnalytics()

    if request.method == "POST":
        produto = Produto.query.get_or_404(id)
        produto.nome = (request.form["nome"],)
        produto.preco = (request.form["preco"],)
        produto.quantidade = (request.form["quantidade"],)
        produto.codigobarra = (request.form["codigobarra"],)
        produto.marca = (request.form["marca"],)
        produto.cor = request.form["cor"]
        db.session.commit()

    analytics = analytics.pesquisa_precos(produto.nome)

    if analytics:
        analytics = sorted(analytics, key=lambda x: x["valor_"])
    return render_template("produto/alterar.html", produto=produto, analytics=analytics)


@bp.route("/search", methods=["POST"])
def search():
    search = f"%{request.form['search']}%"
    produtos = Produto.query.filter(
        (Produto.nome.like(search))
        | (
            Produto.codigobarra.like(search)
            | (Produto.cor.like(search))
            | (Produto.marca.like(search))
        )
    ).all()

    return render_template("produto/index.html", produtos=produtos)

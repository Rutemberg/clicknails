from flask import render_template, request, url_for, redirect
from app.resources.fornecedor import bp
from app.extensions import db
from app.models.fornecedor import Fornecedor


@bp.route("/", methods=("GET", "POST"))
def index():
    fornecedores = Fornecedor.query.all()

    if request.method == "POST":
        novo_fornecedor = Fornecedor(
            nome=request.form["nome"],
            cnpj=request.form["cnpj"],
            telefone=request.form["telefone"],
        )
        db.session.add(novo_fornecedor)
        db.session.commit()
        return redirect(url_for("fornecedor.index"))

    return render_template("fornecedor/index.html", fornecedores=fornecedores)

@bp.route("/<int:id>")
def delete(id):
    fornecedor = Fornecedor.query.get_or_404(id)
    db.session.delete(fornecedor)
    db.session.commit()
    return redirect(url_for("fornecedor.index"))
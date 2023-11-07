from flask import Blueprint

bp = Blueprint('fornecedor', __name__)


from app.resources.fornecedor import routes

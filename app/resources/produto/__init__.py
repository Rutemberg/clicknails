from flask import Blueprint

bp = Blueprint('produto', __name__)


from app.resources.produto import routes

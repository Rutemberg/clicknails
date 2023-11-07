from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.resources.produto import bp as produto_bp
    app.register_blueprint(produto_bp, url_prefix='/produto')
    
    from app.resources.fornecedor import bp as fornecedor_bp
    app.register_blueprint(fornecedor_bp, url_prefix='/fornecedor')
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
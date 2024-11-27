from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    bootstrap = Bootstrap(app)
    app.config.from_object(config_class)
    app.config['UPLOAD_FOLDER'] = 'static'
    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as post_bp
    app.register_blueprint(post_bp, url_prefix='/posts')

    @app.route('/test/')
    def test_page():
        return '<h1>Flask Folder Structure Pattern</h1>'

    return app
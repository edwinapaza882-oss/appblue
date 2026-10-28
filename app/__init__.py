from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_secreta'  # Necesaria para sesiones o formularios

    # Importar y registrar los Blueprints
    from app.auth.routes import auth_bp
    from app.usuarios.routes import usuarios_bp
    from app.productos.routes import productos_bp
    from app.admin.routes import admin_bp
    app.register_blueprint(admin_bp)
    from app.blog.routes import blog_bp
    app.register_blueprint(blog_bp)

    app.register_blueprint(auth_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(usuarios_bp)

    # Ruta principal que redirige al login al iniciar el servidor
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app
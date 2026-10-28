from flask import Blueprint, render_template

productos_bp = Blueprint('productos', __name__, url_prefix='/productos', template_folder='templates')

@productos_bp.route('/')
def listar_productos():
    return render_template('productos.html')
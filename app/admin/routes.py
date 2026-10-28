from flask import Blueprint, render_template

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

@admin_bp.route('/panel')
def panel():
    return "Bienvenido al panel de administracion"
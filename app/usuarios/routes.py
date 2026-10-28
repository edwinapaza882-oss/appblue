from flask import Blueprint, render_template

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')

@usuarios_bp.route('/perfil/<nombre_usuario>')
def perfil(nombre_usuario):
    return render_template('perfil.html', usuario=nombre_usuario)
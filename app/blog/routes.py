from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, url_prefix='/blog', template_folder='templates')

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    # Simulamos títulos de entradas basados en el ID
    entradas = {
        1: "Introducción a Flask y Blueprints",
        2: "Desarrollo Web Modular con Python",
        3: "Gestión de Base de Datos y Formularios"
    }
    titulo_entrada = entradas.get(id, "Entrada no encontrada")
    return render_template('entrada.html', titulo=titulo_entrada, id=id)
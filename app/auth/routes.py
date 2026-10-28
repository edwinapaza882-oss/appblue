from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Captura el usuario ingresado
        usuario = request.form['usuario']
        # Redirige al módulo de usuarios pasando el nombre como parámetro
        return redirect(url_for('usuarios.perfil', nombre_usuario=usuario))

    return render_template('login.html')
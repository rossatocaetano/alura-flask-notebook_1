from app import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Users
from flask_bcrypt import check_password_hash


# --- Rota para acesso à página de Login ---
@app.route('/login')
def login():
    page_title = 'Login - Shelf Life'
    #guardar a página que foi solicitada pelo usuário na variável next_page
    next_page = request.args.get('next_page')
    return render_template('login.html', page_title=page_title, next_page=next_page)


# --- Rota para autenticar as informações inseridas na página de Login ---
@app.route('/authenticate', methods=['POST',])
def authenticate():
    #capturar as informações solicitadas pelo usuário
    user = Users.query.filter_by(nickname=request.form['user']).first()
    password = check_password_hash(user.password, request.form['password']) #verificando a hash da senha criptografada
    #checar se as informações inseridas são iguais às que constam no banco de dados
    if user and password:
        session['user_logged'] = user.nickname
        flash(user.nickname + ' logado com sucesso!')
        next_page = request.form['next_page']
        return redirect(next_page)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


# --- Rota para realizar o Logout ---
@app.route('/logout')
def logout():
    session['user_logged'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))
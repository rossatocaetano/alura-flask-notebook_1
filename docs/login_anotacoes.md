# Login anotações

Criar uma página Jinja para login

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ page_title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}">
  </head>
  <body>
    <div class="container">

        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul id="messages" class="list-unstyled">
                {% for message in messages %}
                    <li class="alert alert-success">{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}

        <h1>Faça seu login</h1>
        <form method="POST" action="{{ url_for('authenticate') }}">
            <input type="hidden" name="next_page" value="{{ proxima or url_for('index') }}">
            <p><label>Nome de usuário:</label> <input class="form-control" type="text" name="user" required></p>
            <p><label>Senha:</label> <input class="form-control" type="password" name="password" required></p>
            <p><button class="btn btn-primary" type="submit">Entrar</button></p>
        </form>
    </div>
</body>
</html>
```

Criar o views_user.py para criar as rotas de login, autenticação e logout

```python
from app import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Users
from flask_bcrypt import check_password_hash

# --- Rota para acesso à página de Login ---
@app.route('/login')
def login():
    page_title = 'Login - Shelf Life'
    #guardar a página que foi solicitada pelo usuário na variável proxima
    next_page = request.args.get('next_page')
    return render_template('login.html', page_title=page_title, next_page=next_page)

# --- Rota para autenticar as informações inseridas na página de Login
@app.route('/authenticate', methods=['POST',])
def autenticar():
    #capturar as informações solicitadas pelo usuário
    user = Users.query.filter_by(nickname=request.form['user']).first()
    password = check_password_hash(user.password, request.form['password']) #verificando a hash da senha criptografada
    #checar se as informações inseridas são iguais às que constam no banco de dados
    if user and password:
        session['usuario_logado'] = user.nickname
        flash(user.nickname + ' logado com sucesso!')
        next_page = request.form['next_page']
        return redirect(next_page)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

# --- Rota para realizar o Logout ---
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))
```
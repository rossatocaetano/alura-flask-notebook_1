# Protegendo o CRUD Anotações

Para proteger as rotas que necessitam ser utilizadas apenas por usuários logados, neste caso as rotas de criar, editar e deletar registros, é necessário verificar se existe na sessão o parâmetro criado para realizar esta checagem, no caso deste exemplo, o parâmetro user_logged, que pode foi definido na rota de autenticação:

```python
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
```

Criar o condicional para verificar se o usuário está logado e, em caso negativo, redirecioná-lo à página de login, enviando também o(s) parâmetro(s) para que, após realizar o login, a pessoa retorne à tarefa que deseje (neste exemplo, exceto no caso de deletar o registro):

1. Para criar registro

```python
if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('login', next_page=url_for('new_register')))
```

1. Para editar registro

```python
if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('login', next_page=url_for('update_page', id=id)))
```

1. Para deletar registro

```python
if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('login'))
```
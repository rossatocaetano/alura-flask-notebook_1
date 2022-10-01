# CRUD Anotações

*Observação: Neste momento não será utilizado o Flask-WTF*

### Habilitar o método Post

1. No Jinja, habilitar o método POST

```html
<form method="post">
    
</form>
```

1. No jinja, fazer referência na propriedade action à função que irá realizar a criação do registro, que neste caso chamamos de “create_register”

```html
<form action="{{ url_for('create_register') }}" method="post">
    
</form>
```

1. No views_food.py

```python
@app.route('/create', methods=['POST',])
def create_register():
    ...
```

### CREATE: Criar registro

Neste exemplo temos o bando de dados Foods que possui as colunas: Id, Food e Expiration

| id | food | expiration |
| --- | --- | --- |
|  |  |  |
|  |  |  |

O formulário no Jinja possui a seguinte estrutura:

```html
<form action="{{ url_for('create_register') }}" method="post">
    <label for="food">Nome do alimento:</label>
    <input type="text" name="food">

    <label for="expiration">Data de vencimento:</label>
    <input type="date" name="expiration">

    <input type="submit">
</form>
```

Neste contexto, realizamos a seguinte estrutura para criar o registro no banco de dados

```python
@app.route('/create', methods=['POST',])
def create_register():
    #requisitar as informações do formulário
    food_name = request.form['food']
    food_date = request.form['expiration']
    
    #verificar se o registro já existe no banco de dados
    food = Foods.query.filter_by(food=food_name).first()
    if food:
				flash('Mensagem de erro')
        return redirect(url_for('index'))
    
    #criar o novo objeto
    new_food = Foods(food=food_name, expiration=food_date)

    #adicionar no banco de dados
    db.session.add(new_food)
    db.session.commit()

    #redirecionar ao index
    return redirect(url_for('index'))
```

### READ: Ler registro

Os registros são recuperados do banco de dados pelo método ‘Nome_do_banco.query.order_by(Nome_do_banco.propriedade)’. 

Os arquivos lidos são passados para o Jinja no render_template.

```python
from flask import render_template, request, redirect, url_for
from app import app, db
from models import Foods

@app.route('/')
def index():
    page_title = 'SHELF LIFE WEB APP'
    list_foods = Foods.query.order_by(Foods.id)
    return render_template('index.html', page_title=page_title, foods=list_foods)
```

A conexão com o banco de dados dependem dos arquivos models.py, [app.py](http://app.py) e config.py, que é mencionado no arquivo [Criar DB Anotações](/docs/criar_db_anotacoes.md).
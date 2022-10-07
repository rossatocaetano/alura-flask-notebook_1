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


### UPDATE: Atualizar registro

No arquivo Jinja index.html, é preciso criar o campo de editar, fazer referência a pagina de edição e também ao ID que irá ser editado ao entrar naquela página

```html
<tbody>
            {% for food in foods %}
            <tr>
                <td>{{ food.id }}</td>
                <td>{{ food.food }}</td>
                <td>{{ food.expiration }}</td>
                <td><a href="{{ url_for('update_page', id=food.id) }}">Editar</a></td>
            </tr>
            {% endfor %}
        </tbody>
```

No arquivo de views do CRUD é preciso capturar o ID para que seja passado ao Jinja que irá editar o conteúdo

```python
# --- UPDATE ----
@app.route('/update/<int:id>')
def update_page(id):
    #filtrar a o id que foi passada ao clicar no editar do index e capturar as informações deste registro
    food = Foods.query.filter_by(id=id).first()
    #retornar a página de edição e possibilitar que as informações filtradas sejam exibidas nesta página
    return render_template('update.html', page_title="Registrar novo alimento", food=food)
```

No arquivo Jinja update.html é preciso criar o formulário já com os values que irão ser atualizados ao clicar e com o campo que importará o id para fazer a query no próximo caminho

```python
<form action="{{ url_for('update_register') }}" method="post">
    <!-- O campo hidden servirá para fazer a query do valor que será atualizado no views do CRUD -->
    <input type="hidden" name="id" value="{{ food.id }}"
    
    <label for="food">Nome do alimento:</label>
    <input type="text" name="food" value="{{ food.food }}">

    <label for="expiration">Data de vencimento:</label>
    <input type="date" name="expiration" value="{{ food.expiration }}">

    <input type="submit">
</form>
```

Depois é necessário criar a função no arquivo de views do Food que está referenciada no form action do Jinja

```python
@app.route('/update_register', methods=['POST',])
def update_register():
    #buscar o id que foi passado na página update da função update_form
    food = Foods.query.filter_by(id=request.form['id']).first()
    #atualizar os valores
    food.food = request.form['food']
    food.expiration = request.form['expiration']
    #registrar as alterações
    db.session.add(food)
    db.session.commit()
    #retornar para página inicial
    return redirect(url_for('index'))
```

### Delete: deletar um registro

Primeiro, é necessário criar o link para deletar no Jinja

```html
<tr>
	<td>{{ food.id }}</td>
	<td>{{ food.food }}</td>
	<td>{{ food.expiration }}</td>
	<td>
		<a href="{{ url_for('update_page', id=food.id) }}">Editar</a>
		<a href="{{ url_for('delete_register', id=food.id) }}">Deletar</a>
	</td>
</tr>
```

Depois, é necessário criar a rota no arquivo de views do CRUD

```python
# --- DELETE ---
@app.route('/delete/<int:id>')
def delete_register(id):
    Foods.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Registro deletado com sucesso')
    return redirect(url_for('index'))
```
# Jinja Anotações

## Criar um template.html no Jinja

### Página com o template.html que será reproduzido nas outras páginas

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Meu app</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}">

    </head>
    <body>
        <div class="container">
            {% block conteudo %}{% endblock %}
        </div>
    </body>
</html>
```

### Página com os arquivos html que herdarão o template.html

```html
{% extends "template.html" %}
{% block conteudo %}

        <h1>Olá Mundo!</h1>
        
{% endblock %}
```

### Inserir variáveis no html

Usar {{ variável }}

```html
{% extends "template.html" %}
{% block conteudo %}

        <h1>{{ app_title }}</h1>

{% endblock %}
```

No arquivo de views, o código ficará da seguinte forma:

```python
@app.route('/')
def home():
    return render_template('index.html', app_title='ola mundo')
```

### Notificações do Bootstrap no Jinja

Inserir no template.html o seguinte bloco:

```html
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

				</div>
</body>
```

A partir dai, já é possível utilizar o método flash no código python

```python
from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos, Usuarios

flash('Olá Mundo!')
        
```
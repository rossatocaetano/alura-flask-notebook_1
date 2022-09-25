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
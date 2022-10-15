# ALURA FLASK NOTEBOOK

## Introdução

Após concluir os estudos do curso de Flask da Alura, senti a necessidade de organizar o conteúdo assistido em exercícios para fixação, abordando os diferentes temas vistos.

**Proposta para este exercício:** Criar um web app que seja capaz de realizar operações CRUD apenas de textos, com senhas criptografadas.

*Observação: Neste momento não será utilizado o Flask-WTF*

**Tema do Web App escolhido:** Realizar um utilitário doméstico para controle do vencimento de alimentos adquiridos 

## Preparando o ambiente

### Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### Criar a estrutura de diretórios

- static
- templates

### Instalar as dependências que serão utilizadas

- Python: v3.10.1
- Flask: v2.0.2
- Bootstrap: v5.1.x okay
- MySQL: v8.0.28
- mysql-connector-python: v8.0.28
- Flask-SQLAlchemy: v2.5.1
- Flask-Bcrypt: v1.0.1

```bash
pip install flask==2.0.2
pip install mysql-connector-python==8.0.28
pip install flask-sqlalchemy==2.5.1
pip install flask-bcrypt==1.0.1
```

<aside>
💡 O Bootstrap pode ser baixo diretamente do site oficial - ou do diretório do Github [https://github.com/alura-cursos/2471-jogoteca-2/blob/master/static/bootstrap.css](https://github.com/alura-cursos/2471-jogoteca-2/blob/master/static/bootstrap.css) 

O arquivo deve ser inserido na pasta “static”

</aside>

### Leia mais

[Gitignore Anotações](/docs/gitignore_anotacoes.md)

[Criar DB Anotações](/docs/criar_db_anotacoes.md)

## Criando a aplicação [Em construção 🏗️]

[Jinja Anotações](/docs/jinja_anotacoes.md)

[CRUD Anotações](/docs/crud_anotacoes.md)

[Login Anotações](/docs/login_anotacoes.md)

[Protegendo o CRUD](/docs/protegendo_o_crud_anotacoes.md)

### Criar a estrutura da aplicação

- config.py [irá receber as configurações necessárias para o funcionamento do app]
- helpers.py [irá receber funções utilitárias do app]
- app.py [irá receber a aplicação]
- models.py [irá receber as classes que serão utilizadas no banco de dados]
- prepara_banco.py [irá ser inserido o script para criação do banco de dados]
- views_food.py [irá receber as rotas de acesso para página]
- views_user.py [irá receber as rotas de acesso do usuário]

## Deploy [Em construção 🏗️]

…

## Referências Bibliográficas

Alura. Flask: avançando no desenvolvimento web com Python. <[https://cursos.alura.com.br/course/flask-desenvolvimento-web](https://cursos.alura.com.br/course/flask-desenvolvimento-web)> - acessado em 12/09/2022.

Documentação MySql para desenvolvedores Pytho. <[https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html](https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html)> - acessado em 25/09/2022. 

Relbeits. ****Hospedagem MySQL Online de Graça e Sem Tempo Limite - Heroku <[https://youtu.be/6ffRYRqt4uc](https://youtu.be/6ffRYRqt4uc)> - acessado em 12/09/2022.

Stackoverflow. Create table with date column. <[https://stackoverflow.com/questions/28041953/create-table-with-date-column](https://stackoverflow.com/questions/28041953/create-table-with-date-column)> - acessado em 25/09/2022
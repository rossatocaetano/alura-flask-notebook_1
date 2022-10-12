# Criar DB Anotações

Para este exercício, com foco em treinar o que foi visto na aula da Alura, o banco de dados escolhido é o MySQL. 

Existirão 2 tabelas: Users e Foods

Users:

| id | name | nickname | password |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

Foods:

| id | food | expiration |
| --- | --- | --- |
|  |  |  |
|  |  |  |

## Criar o banco de dados no MySQL com python

Passo 1 - Importar as dependências que serão utilizadas:

```python
import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash
```

Passo 2 - Conectar ao banco de dados:

```python
print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1', #inserir onde está localizado o bd. Neste caso, na rede local
            user='root', #inserir usuário de acesso ao bd
            password='admin' #inserir senha de acesso ao bd
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `shelf_life`;")

cursor.execute("CREATE DATABASE `shelf_life`;")

cursor.execute("USE `shelf_life`;")
```

Passo 3 - Criar as tabelas:

```python
# criando tabelas
TABLES = {}
#--- alterar os parâmetros conforme as necessidades da tabela a ser criada
TABLES['Foods'] = ('''
      CREATE TABLE `foods` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `food` varchar(50) NOT NULL,
      `expiration` date NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

#--- alterar os parâmetros conforme as necessidades da tabela a ser criada
TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `name` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')
```

Passo 4 - Inserindo valores na tabela users:

```python
# inserindo users
user_sql = 'INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)'
users = [
      ("Administrador", "admin", generate_password_hash("root123").decode('utf-8')), 
#generate password hash gera uma senha que precisa de um hash para descriptografar
      ("Administrador2", "admin2", generate_password_hash("root456").decode('utf-8'))
]
cursor.executemany(user_sql, users)

cursor.execute('select * from shelf_life.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])
```

Passo 5 - Inserindo valores na tabela food:

```python
# inserindo foods
foods_sql = 'INSERT INTO foods (food, expiration) VALUES (%s, %s)'
foods = [
      ('Banana', '2022-10-05'),
      ('Laranja', '2022-10-01'),
      ('Vinho', '2025-04-25'),
]
cursor.executemany(foods_sql, foods)

cursor.execute('select * from shelf_life.foods')
print(' -------------  foods:  -------------')
for food in cursor.fetchall():
    print(food[1])
```

Passo 6 - Commitando os valores:

```python
# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
```

## Criar o models do projeto

### Dependências: config.py e app.py

Criar o config.py, que guardará informações de configurações do APP

```python
SECRET_KEY = 'hello'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'shelf_life'
    )
```

Criar o app.py, que receberá o aplicativo

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views_food import *

if __name__ == '__main__':
    app.run(debug=True)
```

### Config.py

O [config.py](http://config.py) deverá seguir os mesmos parâmetros do bd inseridos no arquivo que criou o banco de dados

```python
from app import db

class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food = db.Column(db.String(50), nullable=False)
    expiration = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Users(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
```
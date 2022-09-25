import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

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
      `senha` varchar(100) NOT NULL,
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


# inserindo users
user_sql = 'INSERT INTO users (name, nickname, senha) VALUES (%s, %s, %s)'
users = [
      ("Administrador", "admin", generate_password_hash("root123").decode('utf-8')),
      ("Administrador2", "admin2", generate_password_hash("root456").decode('utf-8'))
]
cursor.executemany(user_sql, users)

cursor.execute('select * from shelf_life.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

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

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
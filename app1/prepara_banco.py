import pymysql

conn = pymysql.connect(host='localhost',
<<<<<<< Updated upstream
                       user='igor',
                       password='12345')
=======
                       user='root',
                       password='todobancogosta@zika1391')
>>>>>>> Stashed changes

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE `jogoteca`;")
# conn.commit()


# Criando o banco de dados
conn.cursor().execute('CREATE DATABASE IF NOT EXISTS jogoteca')

conn.select_db('jogoteca')

# Criando tabelas no banco
cur = conn.cursor()

cur.execute("CREATE TABLE `jogo` (`id` int NOT NULL AUTO_INCREMENT,`nome` varchar(50) NOT NULL,`categoria` varchar(40)  NOT NULL,`console` varchar(20) NOT NULL,PRIMARY KEY (`id`))")

cur.execute("CREATE TABLE `usuario` (`id` varchar(8) NOT NULL,`nome` varchar(20) NOT NULL,`senha` varchar(8) NOT NULL,PRIMARY KEY (`id`))")

# inserindo usuarios

cur.executemany(
      'INSERT INTO jogoteca.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
<<<<<<< Updated upstream
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
=======
>>>>>>> Stashed changes
            ('igor', 'Igor Szot', '12345')
      ])

cur.execute('select * from jogoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cur.fetchall():
    print(user[1])

# inserindo jogos
cur.executemany(
      'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
      [
            ('God of War 4', 'Ação', 'PS4'),
            ('NBA 2k18', 'Esporte', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Corrida', 'SNES'),
            ('Counter Strike Global Offensive', 'FPS', 'PC'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS'),
      ])

cur.execute('select * from jogoteca.jogo')
print(' -------------  Jogos:  -------------')
for jogo in cur.fetchall():
    print(jogo[1])

conn.commit()
cur.close()
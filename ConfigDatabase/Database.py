import mysql.connector
import logging


class MySQLDatabase:
    # Faz a conexao com meu database
    def conectar_banco(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin123",
                database="api"
            )
            return conexao
        except mysql.connector.Error as e:
            print("Erro ao conectar ao banco de dados!", e)
            return None

    # Test: Recupera o nome do meu database
    def get_database_name(self):
        return self.conectar_banco()._database

    # Test: Recupera a quantidade de tables do meu database via query
    def get_database_tables(self):
        conexao = self.conectar_banco()
        mycursor = conexao.cursor()

        mycursor.execute('Show tables')
        num_tables = mycursor.fetchall()
        return num_tables


    # Testa a conexao do meu database
    def connection_test(self):
        conexao = self.conectar_banco()
        if conexao:
            print("Conexão bem-sucedida!")
            conexao.close()
        else:
            print("Falha na conexão!")


db = MySQLDatabase()
db.connection_test()


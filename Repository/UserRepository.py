from ConfigDatabase.Database import MySQLDatabase
import mysql.connector
import logging


class UserRepository:
    def __init__(self):
        self.db = MySQLDatabase()

    def create_user(self, username, email, first_name, last_name, password_user, identity_user):
        conexao = self.db.conectar_banco()
        mycursor = conexao.cursor()

        query_sql = ("INSERT INTO users (username, email, first_name, last_name, password_user, identity_user) VALUES "
                     "(%s, %s, %s, %s, %s, %s)")

        values = (username, email, first_name, last_name, password_user, identity_user)

        try:
            logging.info("Executando inserção na tabela 'users' com os seguintes valores: %s", values)
            mycursor.execute(query_sql, values)
            conexao.commit()
            logging.info("Inserção bem-sucedida na tabela 'users'")
            return True
        except mysql.connector.Error as e:
            logging.error("Erro ao criar linha na tabela 'users': %s", e)
            conexao.rollback()
            return False
        finally:
            mycursor.close()
            conexao.close()

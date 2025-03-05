import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'senha.123'
        self.database = 'crud_aluno'

    def connect(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def execute_query(self, query, values=None):
        """Executa uma query de insert, update ou delete."""
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query, values or [])
                conn.commit()
                cursor.close()
            except Error as e:
                print(f"Erro ao executar query: {e}")
            finally:
                conn.close()

    def fetchall(self, query):
        """Executa uma query select e retorna todos os resultados."""
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
            except Error as e:
                print(f"Erro ao buscar dados: {e}")
                return []
            finally:
                conn.close()

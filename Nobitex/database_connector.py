import mysql.connector
from context_manager import Context


class send_to_mysql:

  
    def __init__(self, out_key:str, out_value:str):
        self.key = out_key;
        self.value = out_value;
        
    def sql_insertion(self):
        dbconfig = {
            'host' : '127.0.0.1',
            'user' : '',
            'password' : '',
            'database' : 'nobitex',
            }
        with Context(dbconfig) as cursor:
            _SQL = """INSERT INTO current_balance (coin, balance) VALUES (%s, %s)"""
            cursor.execute(_SQL, (self.key, self.value));
            cursor.fetchall();

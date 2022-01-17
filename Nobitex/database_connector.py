import mysql.connector
from context_manager import Context


class send_to_mysql:

  
    def __init__(self, out_key:str ="btc", out_value:str="0.00000"):
        self.key = out_key;
        self.value = out_value;
        
    def sql_insertion(self):
        self.dbconfig = {
            'host' : '127.0.0.1',
            'user' : 'saeedjefe',
            'password' : '#860160Mysql25400#',
            'database' : 'nobitex',
            }
        with Context(self.dbconfig) as cursor:
            _SQL = """INSERT INTO current_balance (asset, balance) VALUES (%s, %s)"""
            cursor.execute(_SQL, (self.key, self.value));
            cursor.fetchall();
            
    def sql_retrieving(self):
        with Context(self.dbconfig) as cursor:
            _SQL = """SELECT * FROM  current_balance """
            cursor.execute(_SQL);
            res = cursor.fetchall();
        return res;
         

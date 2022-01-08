import mysql.connector
import ast
from database_connector import send_to_mysql


class ast_agent:

    def __init__(self, data)-> str:
        self.data = data;
        
    def data_extraction(self):
        dic = ast.literal_eval(self.data)
        for key in dic:
            if key == 'balance':
                self.balance = dic[key];
                self.key = key
                smsql = send_to_mysql(self.key, self.balance);
                smsql.sql_insertion();
            

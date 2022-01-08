import mysql.connector

class Context:

    def __init__(self, dbconfig):
        self.config = dbconfig;
        
    def __enter__(self):
        self.conn = mysql.connector.connect(**self.config);
        self.cursor = self.conn.cursor();
        return self.cursor;
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit();
        self.cursor.close();
        self.conn.close();
        

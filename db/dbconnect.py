import psycopg2
from psycopg2 import extras
from env import dbconfig as configfile

class DBconnect:
    def __init__(self):
        config = configfile.rdb_config
        self.conn = psycopg2.connect(
            user=config['user'], 
            password=config['password'], 
            port=config['port'], 
            host=config['host'], 
            dbname=config['database']
        )
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
       
        self.db_type = "postgres"
        print('RDS postgres db connect')

    def close(self):
        print('RDS postgres db disconnect')
        self.cursor.close()
        self.conn.close()

    def thread_conn_close(self) : 
        self.conn.closeall()

    def get_cursor(self) : 
        return self.cursor

    def get_conn(self) : 
        return self.conn

    def get_db_type(self) : 
        return self.db_type
    
    def get_extras(self) : 
        return psycopg2.extras
    def commit(self):
        self.conn.commit()
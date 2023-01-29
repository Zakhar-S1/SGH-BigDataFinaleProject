import psycopg2
import pandas as pds
from sqlalchemy import create_engine


class PostgreSQLManager:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.df = None

    def connect_to_db(self):
        self.engine = create_engine(
            'postgresql+psycopg2://zahar:zahar@172.20.0.4:5432/postgres'
        )
        self.conn = self.engine.connect()

    def execute_sql_to_xlsx(self, sql, filename):
        print(sql)
        self.df = pds.read_sql(str(sql), self.conn)
        self.df.to_excel(f'./{filename}.xlsx')

    def close_connection(self):
        self.conn.close()

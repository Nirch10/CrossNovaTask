from Task1.WebApp.DbQuery import DbQuery
import psycopg2

class PSqlQuery(DbQuery):
    def __init__(self, host: str, port: int, db_name: str, username: str, password: str):
        super(PSqlQuery, self).__init__(host, port, db_name, username, password)

    def get_2_numerical_columns(self, column_1: str, column_2: str) -> dict:
        connection = psycopg2.connect(user=self.db_user, password= self.db_password,
                                      host=self.db_ip,
                                      port=str(self.db_port),
                                      database=self.db_name)
        cursor = connection.cursor()
        cursor.execute("Select " + column_1 + ", "+ column_2+" from public.auto")
        records = cursor.fetchall()
        results = dict()
        results[column_1] = []
        results[column_2] = []
        for rec in records:
            results[column_1].append(rec[0])
            results[column_2].append(rec[0])
            print(type(rec[0]))
        return results

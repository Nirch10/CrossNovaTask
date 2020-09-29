from Task1.WebApp.DbQuery import DbQuery
import psycopg2


class PSqlQuery(DbQuery):
    def __init__(self, host: str, port: int, db_name: str, username: str, password: str):
        super(PSqlQuery, self).__init__(host, port, db_name, username, password)

    def get_2_numerical_columns(self, column_1: str, column_2: str) -> dict:
        connection = self.__connect_db()
        cursor = connection.cursor()
        cursor.execute("Select " + column_1 + ", " + column_2 + " from public.auto")
        records = cursor.fetchall()
        results = dict()
        results[column_1] = []
        results[column_2] = []
        # print(type(records[column_1][0]))
        # if type(records[column_1][0]) is int or type(records[column_2][0]) is int:
        #     return results
        for rec in records:
            results[column_1].append(rec[0])
            results[column_2].append(rec[0])
        return results

    def get_table_columns(self) -> list:
        connection = self.__connect_db()
        cursor = connection.cursor()
        # cursor.execute(
        #     "SELECT * FROM information_schema.columns WHERE table_schema = 'auto' AND table_name   "
        #     "='public.auto';")
        cursor.execute("select * from public.auto where false")
        results = cursor.description
        columns = []
        for result in results:
            columns.append(result.name)
        return columns

    def __connect_db(self):
        connection = psycopg2.connect(user=self.db_user, password=self.db_password,
                                      host=self.db_ip,
                                      port=str(self.db_port),
                                      database=self.db_name)
        return connection

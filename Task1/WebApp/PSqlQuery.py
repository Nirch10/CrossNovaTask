from Task1.WebApp.DbQuery import DbQuery
import psycopg2


class PSqlQuery(DbQuery):
    def __init__(self, host: str, port: int, db_name: str, username: str, password: str):
        super(PSqlQuery, self).__init__(host, port, db_name, username, password)

    def get_2_numerical_columns(self, column_1: str, column_2: str) -> dict:
        connection = self.__connect_db()
        if connection is None:
            return []
        cursor = connection.cursor()
        cursor.execute("Select " + column_1 + ", " + column_2 + " from public.auto ")
        records = cursor.fetchall()
        results = dict()
        results[column_1] = []
        results[column_2] = []
        for rec in records:
            results[column_1].append(rec[0])
            results[column_2].append(rec[0])
        return results

    def get_table_columns(self, accepted_types: list) -> list:
        """

        :return:List of filtered columns
        """
        in_list_query_str = self.__get_str_from_types(accepted_types)
        connection = self.__connect_db()
        if connection is None:
            return []
        cursor = connection.cursor()
        cursor.execute(
            "SELECT column_name FROM information_schema.columns cols WHERE cols.data_type in (" + in_list_query_str + ") ")
        # cursor.execute("SELECT table_name, column_name FROM information_schema.columns cols WHERE cols.data_type in ("+in_list_query_str+") ")
        results = cursor.fetchall()
        columns = []
        for result in results:
            columns.append(result[0])
        return columns

    def __connect_db(self):
        try:
            connection = psycopg2.connect(user=self.db_user, password=self.db_password,
                                          host=self.db_ip,
                                          port=str(self.db_port),
                                          database=self.db_name)
            return connection
        except Exception:
            return None

    def __get_str_from_types(self, types_list: list) -> str:
        list_as_strings = ''
        for type_str in types_list:
            list_as_strings = list_as_strings + ',\'' + type_str + '\''
        return list_as_strings[1:]

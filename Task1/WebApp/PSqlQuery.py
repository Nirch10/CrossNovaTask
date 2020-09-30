from decimal import Decimal

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
            if isinstance(rec[0], (Decimal, float)) and isinstance(rec[1], (Decimal, float)):
                results[column_1].append(rec[0])
                results[column_2].append(rec[1])
        return results

    def get_table_columns(self, accepted_col_types: list) -> list:
        """
        :param accepted_col_types: list of accepted types to show from table columns
        :return:List of filtered columns
        """
        try:
            in_list_query_str = self.__get_str_from_types(accepted_col_types)
            connection = self.__connect_db()
            if connection is None:
                return []
            cursor = connection.cursor()
            if len(accepted_col_types) > 0:
                return self.__get_columns_by_condition(in_list_query_str, cursor)
            return self.__get_all_columns(cursor)

        except Exception:
            return [];

    def __connect_db(self):
        try:
            connection = psycopg2.connect(user=self.db_user, password=self.db_password,
                                          host=self.db_ip,
                                          port=str(self.db_port),
                                          database=self.db_name)
            return connection
        except Exception:
            return None

    @staticmethod
    def __get_all_columns(cursor) -> list:
        """
        :param cursor:cursor which holds the connection to db
        :return: a list with all table columns
        """
        cursor.execute("SELECT * from public.auto where false")
        query_response_list = cursor.description
        columns = []
        for result in query_response_list:
            columns.append(result.name)
        return columns

    @staticmethod
    def __get_columns_by_condition(accepted_columns_str: str, cursor) -> list:
        """

        :param accepted_columns_str: list of accepted types to show from table columns
        :param cursor: cursor which holds the connection to db
        :return: a list with all table columns whose type are in the accepted_columns
        """
        where_clause = "WHERE cols.data_type in (" + accepted_columns_str + ")"

        cursor.execute(
            "SELECT column_name FROM information_schema.columns cols" + where_clause)
        query_response_list = cursor.fetchall()
        columns = []
        for result in query_response_list:
            columns.append(result[0])
        return columns

    def __get_str_from_types(self, types_list: list) -> str:
        list_as_strings = ''
        for type_str in types_list:
            list_as_strings = list_as_strings + ',\'' + type_str + '\''
        return list_as_strings[1:]

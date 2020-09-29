class DbQuery(object):
    def __init__(self, db_ip: str, db_port: int, db_user: str, db_password: str) -> object:
        self.db_user = db_user
        self.db_port = db_port
        self.db_password = db_password
        self.db_ip = db_ip

    def get_2_numerical_columns(self, column_1: str, column_2: str) -> list:
        """
        :param column_2: str => column_2 name
        :type column_1: str => column_1 name
        :rtype: List containing 2 lists : one for each column's results
        """
        pass

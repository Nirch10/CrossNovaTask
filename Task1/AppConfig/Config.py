import json


class Config(object):
    def __init__(self, json_config_path: str) -> None:
        """
        gets the Config.json file path, and reads its data in to self.attr to use for the whole program
        :param json_config_path:
        """
        with open(json_config_path) as file:
            json_obj = json.load(file)
        self.dbHost = None if 'host' not in json_obj['DBConfig'] else json_obj['DBConfig']['host']
        self.dbPort = None if 'port' not in json_obj['DBConfig'] else json_obj['DBConfig']['port']
        self.dbUserName = None if 'userName' not in json_obj['DBConfig'] else json_obj['DBConfig']['userName']
        self.dbPassword = None if 'password' not in json_obj['DBConfig'] else json_obj['DBConfig']['password']
        self.dbTable = None if 'tableName' not in json_obj['DBConfig'] else json_obj['DBConfig']['tableName']
        self.appIp = None if 'ip' not in json_obj['WebAppConfig'] else json_obj['WebAppConfig']['ip']
        self.appPort = None if 'port' not in json_obj['WebAppConfig'] else json_obj['WebAppConfig']['port']
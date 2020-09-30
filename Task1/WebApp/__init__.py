import os

from Task1.AppConfig.Config import Config
from Task1.WebApp import App


def get_config_path() -> str:
    """
    :return: Config.json file path
    """
    return os.path.realpath('../AppConfig/Config.json')


if __name__ == '__main__':
    config = Config(get_config_path())
    App.start_web_app(config)



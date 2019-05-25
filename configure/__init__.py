import os
from configparser import ConfigParser

class Configure(object):
    @staticmethod
    def get_value(section, option):
        parser = ConfigParser()
        config_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = f'{config_dir}/config.ini'
        config = parser.read(config_file)

        if config:
            value = parser.get(section, option)
            return value
        else:
            print('Config file is not exist')
import json
import os
from src.logger import logger


def load_config(config_path='config\config.json'):
    '''Trying to open a config file and handle errors'''
    try:
        with open(config_path, 'r') as config_file:
            logger.info(f'Downloading the configuration from a file {config_path}')
            return json.load(config_file)
    except FileNotFoundError:
        logger.error(f'The configuration file "{config_path}" was not found')
        return None
    except json.JSONDecodeError:
        logger.error(f'The configuration file "{config_path}" is not a valid JSON file')
        return None

import yaml
import glob
from lib import util
from loguru import logger


def main():
    logger.add('log.log')
    with open('config.yml', 'r') as yml:
        config = yaml.load(yml)

    logger.info('=== start ===')
    logger.info(f'{config["globals"]["dir_save"]}*')



if __name__ == "__main__":
    main()

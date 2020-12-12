import yaml
from loguru import logger


def main():
    logger.add('log.log')
    with open('config.yml', 'r') as yml:
        config = yaml.load(yml)

    logger.info('=== start ===')


if __name__ == "__main__":
    main()

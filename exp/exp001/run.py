import os
import yaml
from glob import glob
from lib import util
from loguru import logger


def init_exp(config):
    # output dirの作成
    _dir = os.path.dirname(os.path.abspath(__file__))
    exp_name = _dir.split('/')[-1]
    dir_exp = f'{config["globals"]["dir_save"]}{exp_name}'
    if not os.path.exists(dir_exp):
        os.makedirs(dir_exp)


def main():
    logger.add('log.log')
    logger.info('=== start ===')
    with open('config.yml', 'r') as yml:
        config = yaml.load(yml)

    # init
    init_exp(config)

    # get features
    X, X_te = util.get_features(config)


if __name__ == "__main__":
    main()

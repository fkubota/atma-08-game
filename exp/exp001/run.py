import os
import yaml
import numpy as np
from lib import util
from lib import trainner
from loguru import logger
from sklearn.model_selection import KFold


def init_exp(config):
    # output dirの作成
    _dir = os.path.dirname(os.path.abspath(__file__))
    exp_name = _dir.split('/')[-1]
    dir_exp = f'{config["globals"]["dir_save"]}{exp_name}'
    if not os.path.exists(dir_exp):
        os.makedirs(dir_exp)

    return dir_exp


def main():
    logger.remove()
    logger.add('log.log', mode='w')
    logger.info('=== start ===')
    with open('config.yml', 'r') as yml:
        config = yaml.load(yml)

    # init
    dir_exp = init_exp(config)

    # get dataset
    train, _, ss = util.get_datasets(config)

    # get features
    X, X_te = util.get_features(config)

    # X, y
    y = train[['Global_Sales']].copy()
    y = np.log1p(y)  # 1 を足してlog を適用

    # splitter
    splitter = KFold(**config['split']['params'])

    # run
    oof, y_test_pred, models = trainner.run_lgbm(X, y, X_te, splitter, config)
    logger.info(f'oof score: {util.metric(np.expm1(y), oof):.5f}')

    # create sub
    util.create_sub(ss, y_test_pred, dir_exp, config)

    # analysis
    util.analysis(models, X, dir_exp)


if __name__ == "__main__":
    main()

import yaml
from pprint import pprint
with open('config.yml', 'r') as yml:
    config = yaml.load(yml)
pprint(config)

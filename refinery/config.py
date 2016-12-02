"""
Config as plain dictionary passed everywhere.

We can form this config from command line arguments and as json file
"""

import json
import argparse


DEFAULT_MODEL_DIR = '/var/local/models/'


default_config = {
    'root_dir': DEFAULT_MODEL_DIR,
    # Will change when model is set.
    'model_name': 'last_model',
    'model_id': 0,
    'description': 'Base model',

    'opt1': 1
}


def save_config(config: dict, filename: str):
    with open(filename, 'w') as fp:
        json.dump(config, fp, ensure_ascii=False, indent=4, sort_keys=True)


def load_config(filename: str) -> dict:
    with open(filename) as fp:
        return json.load(fp)


def get_default_config() -> dict:
    return default_config.copy()


def get_config() -> dict:
    """
    Reads all config from command line (or return default).
    Priority:
    1. command line arg
    2. config file json
    3. default config
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str, help='Config json location.')

    for key in sorted(default_config.keys()):
        parser.add_argument('--' + key, type=type(default_config[key]))

    args = parser.parse_args()
    cfg = get_default_config()
    if args.config:
        upd_config = load_config(args.config)
        cfg.update(upd_config)

    for key, value in vars(args).items():
        if value is not None:
            cfg[key] = value

    return cfg

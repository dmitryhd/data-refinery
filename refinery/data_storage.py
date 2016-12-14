import os
import json
from os.path import join

import pandas as pd

DEFAULT_MODEL_DIR = '/tmp/'


class ModelDataStorage:
    """
    Container class for model.
    All dataframes and sframes (as csv) stored in this model's directory.
    """
    def __init__(self, name: str, root_dir: str = DEFAULT_MODEL_DIR):
        self.name = name
        self.root_dir = root_dir
        self.path = join(self.root_dir, self.name)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        self.log_path = self.path_to('model.log')

    def path_to(self, filename: str) -> str:
        return join(self.path, filename)

    def add_df(self, name: str, df: pd.DataFrame, file_format='hdf', sep=','):
        """ Save dataframe on disk (in model directory). """
        assert isinstance(name, str), 'Wrong usage, pass name first'
        if file_format == 'csv':
            file_path = self.path_to(name + '.csv')
            _df_write_csv(df, file_path, sep=sep)
        elif file_format == 'hdf':
            file_path = self.path_to(name + '.hd5')
            _df_write_hdf(df, file_path)
        else:
            raise Warning('Wrong format. csv or hdf supported.')

    def get_df(self, name: str, file_format='hdf', sep=';') -> pd.DataFrame:
        """ Read dataframe from model directory. """
        if file_format == 'csv':
            file_path = self.path_to(name + '.csv')
            return _df_read_csv(file_path, sep)
        elif file_format == 'hdf':
            file_path = self.path_to(name + '.hd5')
            return _df_read_hdf(file_path)
        else:
            raise Warning('Wrong format. csv or hdf supported.')

    def add_dict(self, info: dict, filename: str):
        file_path = self.path_to(filename) + '.json'
        with open(file_path, 'w') as fd:
            json.dump(info, fd, ensure_ascii=False, indent=4, sort_keys=True)

    def get_dict(self, filename: str) -> dict:
        file_path = self.path_to(filename) + '.json'
        try:
            with open(file_path) as fd:
                return json.load(fd)
        except FileNotFoundError:
            print('{} to not exists'.format(file_path))
            return {}

    def __repr__(self):
        return "<Model {}, dir: {}>".format(self.name, self.path)


def _df_read_csv(filename: str, sep=',') -> pd.DataFrame:
    return pd.read_csv(filename, sep, header=0)


def _df_write_csv(dataframe: pd.DataFrame, filename: str, sep=','):
    dataframe.to_csv(filename, header=True, sep=sep, index=False)


def _df_read_hdf(filename: str) -> pd.DataFrame:
    return pd.read_hdf(filename, 'only')


def _df_write_hdf(dataframe: pd.DataFrame, filename: str):
    dataframe.to_hdf(filename, 'only')

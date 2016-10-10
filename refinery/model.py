import os
from os.path import join

import pandas as pd

DEFAULT_MODEL_DIR = '/tmp/'


class Model:
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

    def add_df(self, name: str, df: pd.DataFrame, format='csv', sep=';'):
        """ Save dataframe on disk (in model directory). """
        assert isinstance(name, str), 'Wrong usage, pass name first'
        if format == 'csv':
            file_path = self.path_to(name + '.csv')
            _df_write_csv(df, file_path, sep=sep)
        else:
            raise Warning('Wrong format. csv or hdf supported.')

    def get_df(self, name: str, sep=';', format='csv') -> pd.DataFrame:
        """ Read dataframe from model directory. """
        if format == 'csv':
            file_path = self.path_to(name + '.csv')
            return _df_read_csv(file_path, sep)
        else:
            raise Warning('Wrong format. csv or hdf supported.')

    def __repr__(self):
        return "<Model {}, dir: {}>".format(self.name, self.path)


def _df_read_csv(filename: str, sep=';'):
    return pd.read_csv(filename, sep, header=0)


def _df_write_csv(dataframe: pd.DataFrame, filename: str, sep=';'):
    dataframe.to_csv(filename, header=True, sep=sep, index=False)

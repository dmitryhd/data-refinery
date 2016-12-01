import os
import unittest
import tempfile

import pandas as pd

from refinery import Model


class TestModel(unittest.TestCase):
    def test_add_df(self):
        temp_dir = tempfile.TemporaryDirectory()
        model = Model('t1', temp_dir.name)
        self.assertTrue(os.path.isdir(model.root_dir))

        df = pd.DataFrame({'a': [1]})
        model.add_df('df1', df)

        df2 = model.get_df('df1')
        self.assertEqual(df.to_dict(), df2.to_dict())

        model.add_df('df2', df, file_format='csv')
        df2 = model.get_df('df2', file_format='csv')
        self.assertEqual(df.to_dict(), df2.to_dict())


    def test_repr(self):
        temp_dir = tempfile.TemporaryDirectory()
        model = Model('t1', temp_dir.name)
        self.assertIn('<Model t1,', str(model))

    def test_wrong_format(self):
        temp_dir = tempfile.TemporaryDirectory()
        model = Model('t2', temp_dir.name)
        df = pd.DataFrame({'a': [1]})
        with self.assertRaises(Warning):
            model.add_df('df1', df, file_format='wrong')
        with self.assertRaises(Warning):
            model.get_df('df1', file_format='wrong')

    def test_model_json(self):
        root_dir = tempfile.TemporaryDirectory()
        model = Model(name='md', root_dir=root_dir.name)

        info = {'value1': 10, 'value2': 'omg'}
        model.add_dict(info, 'info')
        got_info = model.get_dict('info')
        self.assertEqual(got_info, info)

        got_info = model.get_dict('not_exists')
        self.assertEqual(got_info, {})

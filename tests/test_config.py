import unittest
import tempfile
import sys

import refinery.config as cfg


class TestConfig(unittest.TestCase):
    def test_get_config(self):
        sys.argv = ['']
        config = cfg.get_config()
        def_config = cfg.get_default_config()
        self.assertEqual(config, def_config)

        sys.argv = ['', '--opt1', '1']
        config = cfg.get_config()
        def_config = cfg.get_default_config()
        self.assertEqual(config['opt1'], 1)
        del def_config['opt1']
        del config['opt1']
        self.assertEqual(config, def_config)

    def test_config_from_file(self):
        config_file = tempfile.NamedTemporaryFile()
        config_upd = {'model_name': 'new_name'}
        cfg.save_config(config_upd, config_file.name)
        default_config = cfg.get_default_config()
        self.assertNotEqual(default_config['model_name'], 'new_name')

        sys.argv = ['', '--config', config_file.name]
        config = cfg.get_config()
        self.assertEqual(config['model_name'], 'new_name')

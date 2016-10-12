import unittest
import tempfile
import logging

import refinery.log as log
from refinery import Model


class TestLog(unittest.TestCase):
    def setUp(self):
        self.root_dir = tempfile.TemporaryDirectory()
        self.model = Model(name='md', root_dir=self.root_dir.name)

    def tearDown(self):
        logger = logging.getLogger(log.LOGGER_NAME)
        logger.handlers = []

    def test_configure_logger(self):
        logger = log.configure_logger()
        self.assertEqual(len(logger.handlers), 3)

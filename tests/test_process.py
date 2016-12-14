import unittest
import tempfile


from refinery import ModelDataStorage
import refinery.process as process


def temp_storage() -> ModelDataStorage:
    temp_dir = tempfile.TemporaryDirectory()
    storage = ModelDataStorage('t1', temp_dir.name)
    storage.temp_dir = temp_dir
    return storage


class TestProcess(unittest.TestCase):
    def test_downloader(self):
        storage = temp_storage()
        proc = process.Downloader(storage)
        proc.run()

    def test_trainer(self):
        storage = temp_storage()
        proc = process.Trainer(storage)
        proc.run()
        self.assertEqual(proc.info, {})

    def test_both(self):
        storage = temp_storage()
        downloader = process.Downloader(storage)
        trainer = process.Trainer(storage)
        downloader.run()
        trainer.run()
        self.assertEqual(trainer.info, {'stopped': True})

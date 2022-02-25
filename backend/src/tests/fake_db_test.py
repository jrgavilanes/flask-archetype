import unittest

from .. import fake_db


class TestExample(unittest.TestCase):
    def test_fake_db(self):
        self.assertTrue(fake_db.bd != [])

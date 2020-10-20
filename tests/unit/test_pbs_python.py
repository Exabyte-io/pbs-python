import unittest

import pbs

class TestPbsPythonUnit(unittest.TestCase):
    def test_test(self):
        self.assertEquals(pbs.ATTR_q, 'shrug')

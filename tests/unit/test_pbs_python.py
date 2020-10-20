import unittest

import pbs

class TestPbsPythonUnit(unittest.TestCase):
    def test_defines(self):
        self.assertEquals(pbs.ATTR_q, 'destination')
        self.assertEquals(pbs.ATTR_N, 'Job_Name')
        self.assertEquals(pbs.ATTR_j, 'Join_Path')
        self.assertEquals(pbs.ATTR_A, 'Account_Name')
        self.assertEquals(pbs.ATTR_m, 'Mail_Points')
        self.assertEquals(pbs.ATTR_r, 'Rerunable')
        self.assertEquals(pbs.ATTR_M, 'Mail_Users')
        self.assertEquals(pbs.ATTR_l, 'Resource_List')
        self.assertEquals(pbs.SET, 0)
        self.assertEquals(pbs.UNSET, 1)
        self.assertEquals(pbs.INCR, 2)
        self.assertEquals(pbs.DECR, 3)



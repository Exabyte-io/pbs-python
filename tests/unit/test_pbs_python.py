import unittest

import pbs

class TestPbsPythonUnit(unittest.TestCase):
    def test_defines(self):
        self.assertEquals(pbs.ATTR_q, 'destination')

    def test_define_ATTR_N(self):
        self.assertEquals(pbs.ATTR_N, 'Job_Name')

    def test_define_ATTR_j(self):
        self.assertEquals(pbs.ATTR_j, 'Join_Path')

    def test_define_ATTR_A(self):
        self.assertEquals(pbs.ATTR_A, 'Account_Name')

    def test_define_ATTR_m(self):
        self.assertEquals(pbs.ATTR_m, 'Mail_Points')

    def test_define_ATTR_r(self):
        self.assertEquals(pbs.ATTR_r, 'Rerunable')

    def test_define_ATTR_M(self):
        self.assertEquals(pbs.ATTR_M, 'Mail_Users')

    def test_define_ATTR_l(self):
        self.assertEquals(pbs.ATTR_l, 'Resource_List')

    def test_define_SET(self):
        self.assertEquals(pbs.SET, 0)

    def test_define_UNSET(self):
        self.assertEquals(pbs.UNSET, 1)

    def test_define_INCR(self):
        self.assertEquals(pbs.INCR, 2)

    def test_define_DECR(self):
        self.assertEquals(pbs.DECR, 3)

    def test_function_present_pbs_default(self):
        self.assertTrue(hasattr(pbs, 'pbs_default'))

    def test_function_present_pbs_connect(self):
        self.assertTrue(hasattr(pbs, 'pbs_connect'))

    def test_function_present_pbs_disconnect(self):
        self.assertTrue(hasattr(pbs, 'pbs_disconnect'))

    def test_function_present_pbs_statnode(self):
        self.assertTrue(hasattr(pbs, 'pbs_statnode'))

    def test_function_present_pbs_statjob(self):
        self.assertTrue(hasattr(pbs, 'pbs_statjob'))

    def test_function_present_new_attropl(self):
        self.assertTrue(hasattr(pbs, 'new_attropl'))

    def test_function_present_pbs_manager(self):
        self.assertTrue(hasattr(pbs, 'pbs_manager'))

    def test_function_present_new_attrl(self):
        self.assertTrue(hasattr(pbs, 'new_attrl'))

    def test_function_present_pbs_alterjob(self):
        self.assertTrue(hasattr(pbs, 'pbs_alterjob'))

    def test_function_present_pbs_rerunjob(self):
        self.assertTrue(hasattr(pbs, 'pbs_rerunjob'))

    def test_function_present_pbs_deljob(self):
        self.assertTrue(hasattr(pbs, 'pbs_deljob'))

    def test_function_present_pbs_submit(self):
        self.assertTrue(hasattr(pbs, 'pbs_submit'))

    def test_function_present_error(self):
        self.assertTrue(hasattr(pbs, 'error'))

    def test_function_present_new_attropl(self):
        self.assertTrue(hasattr(pbs, 'new_attropl'))




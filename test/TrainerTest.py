'''
Created on

@author: pjhu
'''
import unittest
from Zookeeper.Trainer import Trainer


class Test(unittest.TestCase):


    def setUp(self):
        self.obj = Trainer()
        pass


    def tearDown(self):
        del self.obj
        pass


    def test_trainer(self):
        rtn = "trainer"
        real = self.obj.trainer()
        self.assertEqual(rtn, real)
        pass
    
    def test_action(self):
        rtn = "trainer_action"
        real = self.obj.action()
        self.assertEqual(rtn, real)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
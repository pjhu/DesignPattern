'''
Created on 

@author: pjhu
'''
import unittest
from Zookeeper.Feeder import Feeder

class Test(unittest.TestCase):


    def setUp(self):
        self.obj = Feeder()
        pass


    def tearDown(self):
        del self.obj
        pass


    def test_feeder(self):
        rtn = "feeder"
        real = self.obj.feeder()
        self.assertEqual(rtn, real)
        pass
    
    def test_action(self):
        rtn = "feeder"
        real = self.obj.update()
        self.assertEqual(rtn, real)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
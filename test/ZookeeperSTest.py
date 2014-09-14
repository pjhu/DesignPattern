'''
Created on Sep 9, 2014

@author: pjhu
'''
import unittest
from Zookeeper.ZookeeperS import ZookeeperS

class Test(unittest.TestCase):


    def setUp(self):
        self.obj = ZookeeperS()
        pass


    def tearDown(self):
        del self.obj
        pass


    def test_getFeedMethod(self):
        rst = 'feeder'
        real = self.obj.getFeedMethod()
        self.assertEqual(rst, real)
        pass
    
    def test_getTrainMethod(self):
        rst = 'trainer'
        real = self.obj.getTrainMethod()
        self.assertEqual(rst, real)
        pass
    
    def test_methodChanged(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
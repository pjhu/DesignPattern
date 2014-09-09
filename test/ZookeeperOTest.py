'''
Created on Sep 9, 2014

@author: pjhu
'''
import unittest
from Zookeeper.ZookeeperO import ZookeeperO

class Test(unittest.TestCase):


    def setUp(self):
        self.obj = ZookeeperO()
        pass


    def tearDown(self):
        del self.obj
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
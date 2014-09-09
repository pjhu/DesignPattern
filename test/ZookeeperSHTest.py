'''
Created on Sep 9, 2014

@author: pjhu
'''
import unittest
from Zookeeper.ZookeeperSH import ZookeeperSH
from mock import Mock

class Test(unittest.TestCase):


    def setUp(self):
        subject = Mock()
        self.obj = ZookeeperSH(subject)
        pass


    def tearDown(self):
        del self.obj
        pass

    def test_update(self):
        pass
    
    def test_dosomething(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
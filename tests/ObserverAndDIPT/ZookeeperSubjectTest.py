'''
Created on Sep 9, 2014

@author: pjhu
'''
import unittest
from ObserverAndDIP.ZookeeperSubject import ZookeeperSubject


class Test(unittest.TestCase):


    def setUp(self):
        self.obj = ZookeeperSubject()
        pass


    def tearDown(self):
        del self.obj
        pass


    def test_registerObserver(self):
        rtn = ["expect return value"]
        self.obj.registerObserver(rtn[0])
        real = self.obj.observerList
        self.assertEqual(rtn, real)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
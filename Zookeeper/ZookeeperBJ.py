'''
Created on Sep 9, 2014

@author: pjhu
'''

from IObserver import IObserver
from ZookeeperSubject import ZookeeperSubject

class ZookeeperBJ(IObserver):
    '''
    classdocs
    '''


    def __init__(self, subject):
        '''
        Constructor
        '''
        IObserver.__init__(self, subject)
        self.zooSubject = subject
        self.zooSubject.registerObserver(self)
    
    def update(self, feed, train):
        print "Zookeeper in Beijing: ", feed,train
        self.doSomething(feed,train)
    
    def doSomething(self, feed,train):
        print "do something in Beijing"
        pass
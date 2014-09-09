'''
Created on Sep 9, 2014

@author: pjhu
'''

from IObserver import IObserver

class ZookeeperSH(IObserver):
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
        print "Zookeeper in Shanghai: ", feed,train
        self.doSomething(feed,train)
    
    def doSomething(self, feed,train):
        print "do something in Shanghai"
        pass
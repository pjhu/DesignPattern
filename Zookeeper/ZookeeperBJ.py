'''
Created on Sep 9, 2014

@author: pjhu
'''

from IObserver import IObserver

class ZookeeperBJ(IObserver):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        IObserver.__init__(self)
    
    '''
    def update(self, feed, train):
        print "Zookeeper in Beijing: ", feed,train
        self.doSomething(feed,train)
    
    def doSomething(self, feed,train):
        print "do something in Beijing"
        pass
    '''
        
    #pull
    def update(self, subject, otherArgs):
        print "Zookeeper in Beijing: ", otherArgs
        print subject.getFeedMethod()
        print subject.getTrainMethod()
'''
Created on Sep 9, 2014

@author: pjhu
'''

from IObserver import IObserver

class ZookeeperSH(IObserver):
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
        print "ObserverAndDIP in Shanghai: ", feed,train
        self.doSomething(feed,train)
    
    def doSomething(self, feed,train):
        print "do something in Shanghai"
        pass
    '''
        
    #pull
    def update(self, subject, otherArgs):
        print "ObserverAndDIP in Shanghai: ", otherArgs
        print subject.getFeedMethod()
        print subject.getTrainMethod()

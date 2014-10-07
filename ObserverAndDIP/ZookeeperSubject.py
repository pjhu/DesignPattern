'''
Created on Sep 9, 2014

@author: joseph
'''
from SimpleZookeeper import SimpleZookeeper
from Feeder import Feeder
from Trainer import Trainer

from ISubject import ISubject

class ZookeeperSubject(ISubject):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ISubject.__init__(self)
        self.zoo = SimpleZookeeper()
        
        self.observerList = []
        self.feedM = None
        self.trainM = None
        
    def registerObserver(self, observer):
        self.observerList.append(observer)
    
    def removeObserver(self, observer):
        if observer in self.observerList:
            self.observerList.remove(observer)
    '''
    def notifyObserver(self):
        print "push method"
        print "*****************************************"
        for o in self.observerList:
            o.update(self.feedM, self.trainM)
        print "*****************************************\n"

    def getFeedMethod(self):
        feed = Feeder()
        self.zoo.setStaff(feed)
        return self.zoo.staff()
    
    def getTrainMethod(self):
        train = Trainer()
        self.zoo.setStaff(train)
        return  self.zoo.staff()
    
    def methodChanged(self):
        self.feedM = self.getFeedMethod()
        self.trainM = self.getTrainMethod()
        self.notifyObserver()
        
    def setMethodChanged(self, feed, train):
        self.feedM = feed
        self.trainM = train
        self.notifyObserver()
    '''
    
    #For pull
    def notifyObserver(self):
        print "pull method"
        print "*****************************************"
        for o in self.observerList:
            o.update(self, "otherArgs")
        print "*****************************************\n"

    def getFeedMethod(self):
        return self.feedM
    
    def getTrainMethod(self):
        return self.trainM
        
    def setMethodChanged(self, feed, train):
        self.feedM = feed
        self.trainM = train
        self.notifyObserver()
    
    
if __name__ == "__main__":
    zoo = ZookeeperSubject()
    print zoo.methodChanged()
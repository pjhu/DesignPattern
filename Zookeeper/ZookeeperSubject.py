'''
Created on Sep 9, 2014

@author: joseph
'''
from SimpleZookeeper import SimpleZookeeper
from Zookeeper.Feeder import Feeder
from Zookeeper.Trainer import Trainer

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
    
    def notifyObserver(self):
        for o in self.observerList:
            o.update(self.feedM, self.trainM)
        
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
    
if __name__ == "__main__":
    zoo = ZookeeperSubject()
    print zoo.methodChanged()
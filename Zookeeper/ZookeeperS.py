'''
Created on Sep 9, 2014

@author: joseph
'''
from SimpleZookeeper import SimpleZookeeper
from Zookeeper.Feeder import Feeder
from Zookeeper.Trainer import Trainer

from ZookeeperO import ZookeeperO

class ZookeeperS(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.zoo = SimpleZookeeper()
        
    def getFeedMethod(self):
        feed = Feeder()
        self.zoo.setStaff(feed)
        return self.zoo.staff()
    
    def getTrainMethod(self):
        train = Trainer()
        self.zoo.setStaff(train)
        return self.zoo.staff()
    
    def methodChanged(self):
        feedM = self.getFeedMethod()
        trainM = self.getTrainMethod()
        
        objO = ZookeeperO()
        objO.update(feedM, trainM)
        
    
if __name__ == "__main__":
    zoo = ZookeeperS()
    zoo.methodChanged()
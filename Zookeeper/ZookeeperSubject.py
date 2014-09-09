'''
Created on Sep 9, 2014

@author: joseph
'''
from SimpleZookeeper import SimpleZookeeper
from Zookeeper.Feeder import Feeder
from Zookeeper.Trainer import Trainer

class ZookeeperSubject(object):
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
    
if __name__ == "__main__":
    zoo = ZookeeperSubject()
    print zoo.getFeedMethod()
    print zoo.getTrainMethod()
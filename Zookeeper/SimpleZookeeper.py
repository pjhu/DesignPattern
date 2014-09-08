'''
Created on

@author: pjhu
'''
from Zookeeper.Feeder import Feeder
from Zookeeper.Trainer import Trainer
from Zookeeper.Veterinarian import Veterinarian

class SimpleZookeeper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.fObj = Feeder()
        self.tObj = Trainer()
        self.vObj = Veterinarian()
        self.staffObj = None
        
    def staff_type(self, type):
        if type == 'F':
            return 'feeder'
        elif type == 'T':
            return 'trainer'
        elif type == 'V':
            return 'veterinarian'
    
    def staff_noType(self):
        if type == 'F':
            return self.fObj.feeder()
        elif type == 'T':
            return self.tObj.trainer()
        elif type == 'V':
            return self.vObj.veterinarian()
        
    def setStaff(self, obj):
        self.staffObj = obj
    
    def staff(self):
        return self.staffObj.action()
    
if __name__ == '__main__':
    zoo = SimpleZookeeper()
    
    sObj = Feeder()
    zoo.setStaff(sObj)
    print zoo.staff()
    
    sObj = Trainer()
    zoo.setStaff(sObj)
    print zoo.staff()
    
    sObj = Veterinarian()
    zoo.setStaff(sObj)
    print zoo.staff()
    print 'done'
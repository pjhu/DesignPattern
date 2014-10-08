'''
Created on Oct 7, 2014

@author: pjhu
'''

class ReceiverAC(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.temp = 25
        
    def actionOpen(self):
        print "actionOpen"
        
    def actionClose(self):
        print "actionClose"
        
    def actionAddTemp(self):
        self.temp += 1
        print "actionAddTemp: ", self.temp
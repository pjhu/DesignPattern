'''
Created on Oct 7, 2014

@author: pjhu
'''

class Invoker(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.commandDict = {}
    
    def setCommand(self, strID, commandH):
        self.commandDict[strID] = commandH
            
    def buttonWasPushed(self, strID):
        if self.commandDict.has_key(strID):
            self.commandDict[strID].execute()

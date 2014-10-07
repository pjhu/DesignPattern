'''
Created on Oct 7, 2014

@author: pjhu
'''

class InvokerControler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.commandList = []
    
    def addCommand(self, command):
        self.commandList.append(command)
        
    def runCommand(self):
        for comm in self.commandList:
            comm.execute()
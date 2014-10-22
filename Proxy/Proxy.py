'''
Created on Oct 22, 2014

@author: pjhu
'''


class AbstractSubject(object):  
    def __init__(self):
        pass
    
    def request(self):
        pass 
    
class RealSubject(AbstractSubject): 
    def __init__(self):
        pass
    
    def request(self):
        print 'hi, i am RealSubject' 
        
class ProxySubject(AbstractSubject): 
    def __init__(self):
        self.__rs = RealSubject() 
        
    def request(self):
        self.__beforeRequest()
        self.__rs.request()
        self.__afterRequest()
       
    def __beforeRequest(self):
        print 'prepare....' 
        
    def __afterRequest(self):
        print 'finish....' 
       
if __name__ == '__main__':
    subject = ProxySubject()
    subject.request()
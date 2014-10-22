'''
Created on Oct 22, 2014

@author: pjhu
'''
from inspect import ismodule, isclass, isfunction, ismethod, isbuiltin,\
    isroutine, getmembers, getmodule, getfile, getsource, getsourcefile,\
    getsourcelines, getcallargs

if __name__ == '__main__':
    '''
    print "method 1..."
    from Reflect import Reflect
    obj = globals()["Reflect"]()
    print obj.func()
    print "done 1"
    '''
    
    print "method 2..."
    Reflect = __import__("Reflect")
    print getmembers(Reflect)
    print getmodule(Reflect)
    print getfile(Reflect)
    print getsource(Reflect)
    print getsource(Reflect)
    print getsourcelines(Reflect)
    print ismodule(Reflect), isclass(Reflect.Reflect), isfunction(Reflect.Reflect.test)
    print ismethod(Reflect.Reflect.test), isbuiltin(Reflect.Reflect.test)
    if hasattr(Reflect, "Reflect"):
        obj = getattr(Reflect, "Reflect")()
        if isroutine(obj.func):
            print obj.func()
    print "done 1"
    
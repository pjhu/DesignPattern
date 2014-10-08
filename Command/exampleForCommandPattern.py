'''
Created on Oct 7, 2014

@author: pjhu
'''

if __name__ == '__main__':
    from ReceiverAC import ReceiverAC
    from Invoker import Invoker
    from ConcreteCommandAddTemp import ConcreteCommandAddTemp
    from ConcreteCommandClose import ConcreteCommandClose
    from ConcreteCommandOpen import ConcreteCommandOpen
    
    receiver = ReceiverAC()
    invoker = Invoker()
    
    command = ConcreteCommandOpen(receiver)
    invoker.setCommand("OPEN", command)
    command = ConcreteCommandAddTemp(receiver)
    invoker.setCommand("ADD", command)
    command = ConcreteCommandClose(receiver)
    invoker.setCommand("CLOSE", command)
    
    invoker.buttonWasPushed("OPEN")
    invoker.buttonWasPushed("ADD")
    invoker.buttonWasPushed("ADD")
    invoker.buttonWasPushed("ADD")
    invoker.buttonWasPushed("ADD")
    invoker.buttonWasPushed("ADD")
    invoker.buttonWasPushed("CLOSE")
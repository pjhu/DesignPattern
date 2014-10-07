'''
Created on Oct 7, 2014

@author: pjhu
'''

if __name__ == '__main__':
    from ReceiverTV import ReceiverTV
    from InvokerControler import InvokerControler
    from ConcreteCommandChange import ConcreteCommandChange
    from ConcreteCommandClose import ConcreteCommandClose
    from ConcreteCommandOpen import ConcreteCommandOpen
    
    receiver = ReceiverTV()
    invoker = InvokerControler()
    
    command = ConcreteCommandOpen(receiver)
    invoker.addCommand(command)
    invoker.runCommand()
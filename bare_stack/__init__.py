import inspect
import pprint
from termcolor import colored

def bare_stack():
    for frame in inspect.stack()[1:]:
        args, varargs, varkw, locals = inspect.getargvalues(frame.frame)
        args = inspect.formatargvalues(args, varargs, varkw, locals)
        
        filename = "{}:{}".format(frame.filename, frame.lineno)
        print(colored("{:>80}".format(filename[-80:]), "grey"), colored(frame.function, "blue"))
        pprint.pprint(args, indent=4)
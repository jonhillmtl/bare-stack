import inspect

def bare_stack():
    for frame in inspect.stack():
        args, varargs, varkw, locals = inspect.getargvalues(frame.frame)
        args = inspect.formatargvalues(args, varargs, varkw, locals)
        
        print("{} ({}): {}({})".format(
            frame.filename, 
            frame.lineno, 
            frame.function, 
            args))
    
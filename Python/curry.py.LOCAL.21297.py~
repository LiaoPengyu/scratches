def curry(f, *args, **kwargs):
    """
    f should be callable
    """
    argCount, argNames = (lambda c, l: (c.co_argcount - l, c.co_varnames[:-l])) \
                       (f.func_code, len(f.func_defaults or ()))
    def curried(*targs, **tkwargs):
        targs += args
        tkwargs.update(kwargs)
        if len(targs) + len(set(tkwargs.keys()) & set(argNames)) >= argCount:
            return f(*targs, **tkwargs)
        return curry(f, *targs, **tkwargs)
    return curried

@curry
def test(a,b,c,d=1,e=2):
    print a,b,c,d,e

test(5,b = 4, d=3, e=2)(c = 1)
test(c=1, e=2)(3, d=4)(5)

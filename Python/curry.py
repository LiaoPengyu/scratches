
def curry(f, *args, **kws):
    # 判断是否为第一次柯里化：
    argsDict = f.__dict__.get("argsDict")
    kwsDict  = f.__dict__.get("kwsDict")
    if not (argsDict or kwsDict):
        fcode, kwsVals     = f.func_code, f.func_defaults
        varNames, varCount = fcode.co_varnames, fcode.co_argcount
        if not varCount: # 无参函数直接返回
            return f
        argsNum   = varCount - len(kwsVals) # 非关键字参数个数
        argsNames = varNames[:argsNum - 1]  # 非关键字参数名
        argsDict = dict(zip(varNames,          # 非关键字参数，
                            argsNum * [None])) # 注意:非关键字参数也可以按关键字参数方式传入
        kwsDict = dict(zip(reversed(varNames), # 关键字参数
                           reversed(kwsVals)))
    def curried(*cargs, **ckws):

        nargs, nkws = args+fargs, kws.copy()
        nkws.update(fkws)
        if len(nargs)+len(nkws) >= nonkws:
            return f(*nargs, **nkws)
        return curry(f, *nargs, **nkws)
    curried.__name__ = f.__name__
    return curried

@curry
def a(a,b,c = 1,d = 2):
    return a + b + c + d

print a(1)
print a(1)(2, d = 3)
print a(1,2)
print a(1,2,3)
print a(1, d = 2)(2)

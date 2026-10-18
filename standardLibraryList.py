from headers import *

def f(name:str,args:dict[str,str],returnType:str):
    return FunctionEntry(name,args,returnType)
def getFunctionList() -> list[FunctionEntry]:
    return [
            f("HALT",{},"NULL"),
            ]

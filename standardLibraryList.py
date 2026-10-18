from headers import *

def f(name:str,args:dict[str,str],returnType:str):
    return FunctionEntry(name,args,returnType)
def getFunctionList() -> list[FunctionEntry]:
    return [
            f("PRINT",{"msg":"STR"},"NULL"),
            f("HALT",{},"NULL"),
            ]

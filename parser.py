from headers import *

tokens: list[str] = []
treeStack: list[Compound] = []
genName = ""
functions: list[FunctionEntry] = []

def addFunction(entry:FunctionEntry):
    if entry.name not in [i.name for i in functions]:
        functions.append(entry)
    else:
        raise Exception(f" THE COMPILER IS HEAVILY DISAPPOINTED IN YOUR CREATIVITY WHILE NAMING FUNCTIONS\n FUNCTION {entry.name} COULD PROBABLY USE A UNIQUE NAME")

def setNextGenericName(name:str):
    global genName
    genName = name

def openCompound(name:str):
    global genName
    if name == "generic":
        if genName != "":
            name = genName
            genName = ""
    treeStack.append(Compound(name))

def closeCompound():
    closed = treeStack.pop(-1)
    if len(treeStack) < 1:
        raise Exception(" THE COMPILER WILL NOT TOLERATE EXCESS STATEMENT CLOSURES!")
    treeStack[-1].innerStatements.append(closed)

def addLeaf(leaf:Leaf):
    treeStack[-1].innerStatements.append(leaf)

def popToken() -> str:
    return tokens.pop(0)

def execHandler(name:str):
    func = globals().get(f"handle_{name}")
    if func != None and callable(func):
        _ = func()
    elif name in [i.name for i in functions]:
        callHandler(name)
    else:
        raise Exception(f" COMPILER HAS CHOSEN VIOLENCE BECAUSE OF YOUR NEGLIGENCE WITH SYMBOLS!\n ERROR ON SYMBOL: {name}\n UNKNOWN SYMBOL")

def callHandler(name:str):
    leaf = Leaf(name=f"call_{name}")
    i = popToken()
    while i != "SEMICOLON":
        leaf.args.append(i)
        i = popToken()
    addLeaf(leaf)

def parse(tokenList:list[str],stdlib:list[FunctionEntry]) -> Compound:
    global tokens
    tokens = tokenList
    functions.extend(stdlib)
    openCompound("WORLD")
    while len(tokens) != 0:
        execHandler(tokens.pop(0))
    print(functions)
    return treeStack[0]

def handle_CLASS():
    raise Exception(" did you just try to declare a class? \n not on my watch you idiot.")

def handle_FUNC():
    funcReturnType = popToken()
    funcName = popToken()
    funcArgs = {}
    if popToken() == "OPENPAR":
        arg = False 
        argType = ""
        i = popToken()
        while i != "CLOSEPAR":
            if i != "COMMA":
                if arg:
                    funcArgs[argType] = i
                    arg = not arg 
                else:
                    argType = i
                    arg = not arg
            i = popToken()
    else:
        raise Exception(f" The compiler is confused on the arguments of the function {funcName}")
    setNextGenericName(f"func_{funcName}")
    entry = FunctionEntry(name=funcName,args=funcArgs,returnType=funcReturnType)
    addFunction(entry)

def handle_OPENSTATEMENT():
    openCompound("generic")

def handle_CLOSESTATEMENT():
    closeCompound()

def handle_PYCALL():
    pass # TODO: handle pycalls

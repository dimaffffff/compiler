from dataclasses import dataclass,field

@dataclass 
class leaf:
    name:str = "INVALID_LEAF"
    args:list[str] = field(default_factory=list)

@dataclass 
class compound:
    name:str = "GenericCompound"
    innerStatements:list[compound] = field(default_factory=list)

def execHandler(name:str):
    func = globals().get(f"handle_{name}")
    if func != None and callable(func):
        _ = func()
    else:
        raise Exception(f"\n COMPILER HAS CHOSEN VIOLENCE BECAUSE OF YOUR NEGLIGENCE WITH TOKENS!\n ERROR ON TOKEN: {name}\n UNKNOWN TOKEN")

def handle_CLASS():
    raise Exception(f"\n did you just try to declare a class? \n not on my watch you idiot.")

def parse(tokenList:list[str])-> list[compound|leaf]:
    tokens = tokenList
    while len(tokens) != 0:
        execHandler(tokens.pop(0))
    return []

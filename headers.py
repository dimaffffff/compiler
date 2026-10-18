from dataclasses import dataclass,field


@dataclass 
class FunctionEntry:
    name: str 
    args: dict[str,str]
    returnType: str

@dataclass 
class Leaf:
    name:str = "INVALID_LEAF"
    args:list[str] = field(default_factory=list)

@dataclass 
class Compound:
    name:str = "GenericCompound"
    innerStatements:list[Compound|Leaf] = field(default_factory=list)



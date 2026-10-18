from fileReader import getCode
from lexer import lex

CODE = getCode()
TOKENS = lex(CODE)
print(TOKENS)

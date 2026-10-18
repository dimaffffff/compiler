from fileReader import getCode
from lexer import lex
import parser

CODE = getCode()
TOKENS = lex(CODE)
print(TOKENS)
STAGE1 = parser.parse(TOKENS)
print(STAGE1)

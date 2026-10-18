from fileReader import getCode
from lexer import lex
import parser
from sys import stderr


ERRORCOLOR = "\033[1;31m"
RESET = "\033[0m"
BLINK = "\033[5m"

try:
    CODE = getCode()
    TOKENS = lex(CODE)
    print(TOKENS)
    STAGE1 = parser.parse(TOKENS)
    print(STAGE1)
    print("The compiler has spared you for now.\nCompilation Successful")
except Exception as e:
    print(f"{ERRORCOLOR}{e} \n {BLINK}COMPILATION TERMINATED{RESET}",file=stderr)

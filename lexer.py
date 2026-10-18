def lex(code:str) -> list[str]:
    tokens = lexLine(code) #technically I was supposed to lex line by line but um yeah
    return tokens

def lexLine(line:str) -> list[str]:
    lineTokens: list[str] = []
    running = True 
    currentChar = -1
    while running:
        word: list[str] = []
        additionalToken: str|None = None
        insideStrLit = False
        while True:
            currentChar += 1
            if currentChar >= len(line):
                running = False 
                break
            i = line[currentChar]
            if not insideStrLit:
                match i:
                    case " ":
                        break 
                    case "\n":
                        break
                    case "/":
                        if line[currentChar+1] == "/":
                            comment = True
                            currentChar += 1
                            while comment:
                                currentChar += 1
                                if line[currentChar] == "/" and line[currentChar-1] == "/":
                                    comment = False
                            currentChar += 1
                            i = line[currentChar] #manual override as a hack
                    case ";":
                        additionalToken = "SEMICOLON"
                        break
                    case "{":
                        additionalToken = "OPENSTATEMENT"
                        break
                    case "}":
                        additionalToken = "CLOSESTATEMENT"
                        break
                    case "(":
                        additionalToken = "OPENPAR"
                        break
                    case ")":
                        additionalToken = "CLOSEPAR"
                        break
                    case _:
                        pass

            if i == "\"":
                insideStrLit = not insideStrLit
            else:
                word.append(i)
    
        wordstr = "".join(word) 
        if wordstr != '' and wordstr != '\n':
            lineTokens.append(wordstr)
        word = []
        if additionalToken is not None:
            lineTokens.append(additionalToken)

    return lineTokens

# def getToken(word:str) -> str:
#     mapping: dict[str,str] = {        
#         "#DEFINE":"PREPROC_DEFINE",
#         "#STRUCT":"PREPROC_STRUCT",
#         "FUNC":"FUNC_DEF",
#         "STRUCT":"STRUCT_VAR_DECL",
#         "INT"
# }
#     if word in mapping.keys():
#         return mapping[word]
#     return f"NAME_{word}"

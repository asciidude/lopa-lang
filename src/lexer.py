import re

class Lexer:
    def __init__(self, source):
        self.source = source
    
    def tokenize(self):
        # Initalize variables
        tokens = []
        index = 0

        while index < len(self.source):
            word = self.source[index]

            if word == 'var':
                tokens.append(['VARIABLE_DECLARATOR', word])

            elif re.match('[a-zA-Z]', word):
                if word[len(word) - 1] == ';':
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            elif word[0] == '"':
                buffer = []

                if word[len(word) - 1] != ';':
                    while word[len(word) - 1] != '"':
                        buffer.append(word)
                        
                        index += 1
                        word = self.source[index]

                    buffer.append(word)
                else:
                    buffer.append(word[0:len(word) - 1])

                tokens.append(['STRING', ''.join(buffer)])

            elif re.match('-?[0-9]', word):
                if word[len(word) - 1] == ';':
                    tokens.append(['NUMBER', word[0:len(word) - 1]])
                else:
                    tokens.append(['NUMBER', word])
            elif word in '=/*=-+':
                tokens.append(['OPERATOR', word])

            if word[len(word) -1] == ";":
                tokens.append(['END', ';'])

            index += 1

        return tokens
from tkinter.tix import INTEGER


class Parser:
    def __init__(self, tokens, output):
        self.tokens = tokens
        self.index = 0
        self.transpiled = '# Generated with lopa-lang\n# If you want to use lopa-lang, go to https://www.github.com/asciidude/lopa-lang\n\n'
        self.output = output

    def parse(self):
        while self.index < len(self.tokens):
            # Stores token types
            t_type  = self.tokens[self.index][0]

            # Stores value of token
            t_value = self.tokens[self.index][1]

            if t_type == "VARIABLE_DECLARATOR" and t_value == 'var':
                self.parse_variable_declarator(self.tokens[self.index:len(self.tokens)])

            elif t_type == "IDENTIFIER" and t_value == 'output':
                self.parse_output_statement(self.tokens[self.index:len(self.tokens)])
            elif t_type == "IDENTIFIER" and t_value == 'endproc':
                self.parse_endproc(self.tokens[self.index:len(self.tokens)])

            self.index += 1
    
    def generateFile(self):
        with open(self.output, 'w') as f:
            f.write(self.transpiled)

    # All the parser functions q(≧▽≦q)
    def parse_variable_declarator(self, stream):
        check = 0

        name     = ''
        operator = ''
        value    = ''

        for token in range(0, len(stream)):
            t_type = stream[check][0]
            t_value = stream[check][1]

            if t_type == 'END':
                break

            elif token == 1 and t_type == 'IDENTIFIER':
                name = t_value
            elif token == 1 and t_type != 'IDENTIFIER':
                print(f'ERR -> Failed to parse, invalid variable name \'{t_value}\'')
                quit(-1)

            elif token == 2 and t_type == 'OPERATOR':
                operator = t_value
            elif token == 2 and t_type != 'OPERATOR':
                print(f'ERR -> Failed to parse, assignment operator is missing or invalid on the declaration of a variable')
                quit(-1)

            elif token > 2 and t_type in ['STRING', 'NUMBER', 'IDENTIFIER', 'OPERATOR']:
                value += t_value
            elif token > 2 and t_type not in ['STRING', 'NUMBER', 'IDENTIFIER', 'OPERATOR']:
                print(f'ERR -> Failed to parse, invalid assignment value, {t_value}')
                quit(-1)

            check += 1

        self.transpiled += f'{name} {operator} {value}\n'
        self.index += check

    
    def parse_output_statement(self, stream):
        check = 0
        value = ''

        for token in range(0, len(stream)):
            t_type = stream[check][0]
            t_value = stream[check][1]

            if t_type == 'END':
                break

            elif token > 0 and t_type in ['STRING', 'NUMBER', 'IDENTIFIER', 'OPERATOR']:
                value += t_value
            elif token > 0 and t_type not in ['NUMBER', 'IDENTIFIER', 'OPERATOR']:
                print(f'ERR -> Failed to parse, invalid assignment value, {t_value}')
                quit(-1)

            check += 1

        self.transpiled += f'print({value})\n'
        self.index += check

    
    def parse_endproc(self, stream):
        check = 0
        code = 0

        for token in range(0, len(stream)):
            t_type = stream[check][0]
            t_value = stream[check][1]

            if t_type == 'END':
                break

            elif token == 1 and t_type == 'NUMBER':
                if '.' in t_value:
                    print(f'ERR -> Failed to parse, cannot quit program on a decimal number')
                    quit(-1)

                code = t_value
            elif token == 1 and t_type not in ['NUMBER', None]:
                print(f'ERR -> Failed to parse, cannot parse value {t_value} on \'endproc\'')
                quit(-1)

            check += 1

        self.transpiled += f'quit({code})\n'
        self.index += check
import lexer as l
import parser as p

with open('main.lopa', 'r') as f:
    #################
    #     LEXER     #
    #################
    contents = [i for j in f.read().split() for i in (j, ' ')][:-1]
    lexer = l.Lexer(contents)
    tokens = lexer.tokenize()
    
    ################
    #    PARSER    #
    ################
    parser = p.Parser(tokens)
    parser.parse()
    parser.generateFile('main.py')
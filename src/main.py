import lexer as l
import parser as p
import typer as t

app = t.Typer()

@app.command()
def main(input: str, output: str):
    with open(input, 'r') as f:
        #################
        #     LEXER     #
        #################
        contents = [i for j in f.read().split() for i in (j, ' ')][:-1]
        lexer = l.Lexer(contents)
        tokens = lexer.tokenize()

        ################
        #    PARSER    #
        ################
        parser = p.Parser(tokens, output)

        parser.parse()
        parser.generateFile()

app()
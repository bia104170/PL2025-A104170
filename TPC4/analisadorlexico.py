import sys
import re 
import ply.lex as lex


tokens = (
    'SELECT', 
    'WHERE', 
    'LIMIT', 
    'VAR', 
    'CLASSE', 
    'NUMBER', 
    'STRING', 
    'POINT', 
    'LBRACE', 
    'RBRACE',
    'TYPE'
    )

t_SELECT = r'(?i)select'
t_WHERE = r'(?i)where'
t_LIMIT = r'(?i)limit'
t_POINT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_TYPE = r'\ba\b'

def t_VAR(t):
    r'\?[a-zA-Z_]\w*'
    return t

def t_CLASSE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*:[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_STRING(t):
    r'\".*?\"(@[a-zA-Z]+)?'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass # descartar os comentários

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# criar o lexer
lexer = lex.lex()


def test_lexer(data):
    lexer.input(data)
    for tok in lexer:
        print(tok)

def main():

    query = sys.stdin.read()

    test_lexer(query)

if __name__ == "__main__":
    main()
import ply.lex as lex

tokens = ['NUMBER','OP1','OP2']

def t_OP1(t): # para o * e /
    r'[\/\*]'
    return t

def t_OP2(t): # para o + e -
    r'[\+\-]'
    return t

def t_NUMBER(t): 
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Carácter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex() # construir o lex

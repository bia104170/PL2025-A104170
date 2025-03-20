from anlexico import lexer
from nodo import Exp,Nodo,calculaSoma

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ",simb)

def rec_NUM():
    global prox_simb
    if prox_simb.type == 'NUMBER':
        numero = int(prox_simb.value)
        prox_simb = lexer.token()
        return Nodo(False,numero)
    else:
        parserError(prox_simb)
        return Nodo()

def rec_OP1():
    global prox_simb
    if prox_simb.type == 'OP1':
        op = prox_simb.value
        prox_simb = lexer.token()
        return op
    else:
        parserError(prox_simb)
        return ""

def rec_OP2():
    global prox_simb
    if prox_simb.type == 'OP2':
        op = prox_simb.value
        prox_simb = lexer.token()
        return op
    else:
        parserError(prox_simb)
        return ""

# P5: EP -> OP1 NUMBER EP
# P6: EP    |
def rec_EP(esq):
    global prox_simb

    # P6
    if prox_simb is None or prox_simb.type == 'OP2':
        print("A derivar por P6: EP --> ")
        res = esq
        print("Reconheci P6: EP --> ")
    # P5
    elif prox_simb.type == 'OP1':
        print("A derivar por P5: EP -> OP1 NUMBER EP")
        op = rec_OP1()
        numero = rec_NUM()
        res = rec_EP(Exp(op,esq,numero))
        print("Reconheci P5: EP -> OP1 NUMBER EP")

    else:
        parserError(prox_simb)
        res =  Nodo()
    return res

# P4: EPInicio -> NUMBER EP
def rec_EPI():
    global prox_simb
    print("A derivar por P4: EPInicio -> NUMBER EP")
    numero = rec_NUM()
    res = rec_EP(numero)
    print("Reconheci P4: EPInicio --> NUMBER EP")
    return res

# P2: EN -> OP2 EPInicio EN
# P3: EN    |
def rec_EN(esq):
    global prox_simb

    # P3
    if prox_simb is None:
        print("A derivar por P3: EN -> ")
        res = esq
        print("Reconheci P3: EN -> ")
    # P2
    elif prox_simb.type == 'OP2':
        
        print("A derivar por P2: EN -> OP2 EPInicio EN")
        op = rec_OP2()
        numero = rec_EPI()
        res = rec_EN(Exp(op, esq,numero))
        print("Reconheci P2: EN -> OP2 EPInicio EN")
    
    else:
        parserError(prox_simb)
        res =  Nodo()
    return res

# P1: Inicio -> EPInicio EN
def rec_Inicio():
    global prox_simb
    print("A derivar por P1: Inicio -> EPInicio EN")
    numero = rec_EPI()
    res = rec_EN(numero)
    print("Reconheci P1: Inicio -> EPInicio EN")
    return res

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    arvore = rec_Inicio()
    return calculaSoma(arvore)[1]
    
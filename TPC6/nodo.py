class Exp:
    def __init__(self, op, esq, dir):
        self.op = op
        self.esq = esq
        self.dir = dir

    def __str__(self):
        return f"({self.op} {self.esq} {self.dir})"

class Nodo:
    def __init__(self, isEmpty=True, num=0):
        self.isEmpty = isEmpty
        self.num = num

    def __str__(self):
        if self.isEmpty == True:
            return "()"
        else:
            return f"({self.num})"
        
def calculaSoma(arvore):
    
    if isinstance(arvore, Nodo):
        
        if arvore.isEmpty:
            return (False,0)
        else:
            return (True, arvore.num)
        
    elif isinstance(arvore, Exp):
        op = arvore.op
        esq = calculaSoma(arvore.esq)
        dir = calculaSoma(arvore.dir)
        
        if esq[0] == False and dir[0] == False:
            return (False,0)
        
        elif esq[0] == False and dir[0] == True:
            return dir
        
        elif esq[0] == True and dir[0] == False:
            return esq
        
        else: # esquerda e direita válidos
                        
            match op:
                case '+':
                    valor = esq[1] + dir[1]
                case '-':
                    valor = esq[1] - dir[1]
                case '*':
                    valor = esq[1] * dir[1]
                case '/':
                    valor = esq[1] / dir[1]
                case _: # default
                    return (False, 0)
            
            return (True, valor)
        
        
    else:
        return (False, 0)
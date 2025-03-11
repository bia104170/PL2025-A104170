import json
import ply.lex as lex
import re

tokens = (
            "LISTAR",
            "MOEDA",
            "SELECIONAR",
            "ADICIONAR",
            "SAIR"     
        )

t_LISTAR = r'LISTAR'
t_SAIR = r'SAIR'

def t_MOEDA(t):
    r'MOEDA\s+((\d+[ec](,\s*)?)+)\s+\.'
    t.value = t.value.rstrip(".")
    t.value = t.value[6:].replace(" ", "").split(",")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+([A-Z0-9]+)'
    t.value = t.value.split()[1] # obter o código do produto
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s+([A-Z0-9]+)\s+(\d+)'
    parametros = t.value.split()
    t.value = (parametros[1], int(parametros[2])) # tuplo com o código do produto e a quantidade a adicionar
    return t

t_ignore = " \t"

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex() # criar o lexer

def carregaStock():
    with open("stock.json", "r", encoding="utf-8") as f:
        stock = json.load(f)
    return stock

def atualizaStock(stock):
    with open("stock.json", "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

def listarProdutos(stock):
    print(f"{'COD':<8} | {'NOME':<20} | {'QUANTIDADE':>10} | {'PREÇO (€)':>8}")
    print("--------------------------------------------------------")
    
    for item in stock:
        print(f"{item['cod']:<8}   {item['nome']:<20}   {item['quant']:>10}   {item['preco']:>8.2f}€")

def procuraProduto(codigo, stock):
    for item in stock:
        if item['cod'] == codigo:
            return item
    return None

def imprimir(valor):
    euros = valor // 100
    centimos = valor % 100
    if euros > 0 and centimos > 0:
        return f"{euros}e{centimos}c"
    elif euros > 0:
        return f"{euros}e"
    else:
        return f"{centimos}c"

def selecionaProduto(codigo, saldo, stock):
    produto = procuraProduto(codigo, stock)
    if produto:

        if produto['quant'] == 0:
            print("Produto sem stock.")

        elif saldo < int(produto['preco'] * 100):
            print("Saldo insuficiente para satisfazer o seu pedido.")
            valor = int(produto['preco'] * 100)
            print(f"Saldo = {imprimir(saldo)}; Pedido = {imprimir(valor)}")

        else:
            produto['quant'] -= 1
            saldo -= int(produto['preco'] * 100)
            print(f"Pode retirar o produto dispensado \"{produto['nome']}\"")
            print(f"Saldo = {imprimir(saldo)}")
    else:
        print("Produto selecionado não existe.")
    
    return saldo, stock

moedasDisponiveis = {
                    "2e": 200,
                    "1e": 100, 
                     "50c": 50,
                     "20c": 20,
                     "10c": 10,
                     "5c": 5,
                     "2c": 2,
                     "1c": 1}

# calcula o saldo através das moedas inseridas
def calculaSaldo(moedas, saldo):
    for moeda in moedas:
        if moeda in moedasDisponiveis:
            saldo += moedasDisponiveis[moeda]
        else:
            print("Moeda inválida.")

    print(f"Saldo = {imprimir(saldo)}")

    return saldo

def retornaTroco(saldo):
    if saldo < 0:
        print("Saldo insuficiente para satisfazer o seu pedido.")
        return None
    troco = saldo
    trocoMoedas = {} # guardar a quantidade de moedas para o troco

    for moeda in moedasDisponiveis.values():
        if troco >= moeda:
            trocoMoedas[moeda] = troco // moeda # quantas moedas cabem no troco
            troco = troco % moeda # restante
    
    trocoEcra = []
    for moeda, quantidade in trocoMoedas.items():
        if moeda >= 100:
            trocoEcra.append(f"{quantidade}x {moeda // 100}e")    
        else:
            trocoEcra.append(f"{quantidade}x {moeda}c")
            
    print("Pode retirar o troco: " + ", ".join(trocoEcra) + ".")


def adicionaProduto(parametros, stock):
    produto = procuraProduto(parametros[0], stock)
    if produto:
        produto['quant'] += parametros[1]
        print(f"Produto '{produto['nome']}' atualizado. Nova quantidade: {produto['quant']}.")
    else:
        print("Produto não encontrado.")
    return stock

def maquinaVending():
    stock = carregaStock()
    saldo = 0
    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip()

        lexer.input(comando)

        tokens = []
        for token in lexer:
            #print(token.value)
            tokens.append(token)
            

        if not tokens:
            print("Comando inválido.")
            continue
            
        if tokens[0].type == "LISTAR":
            listarProdutos(stock)

        elif tokens[0].type == "MOEDA":
            saldo = calculaSaldo(tokens[0].value, saldo)

        elif tokens[0].type == "SELECIONAR":
            saldo, stock = selecionaProduto(tokens[0].value, saldo, stock)
        
        elif tokens[0].type == "ADICIONAR":
            stock = adicionaProduto(tokens[0].value, stock)

        elif tokens[0].type == "SAIR":
            if saldo > 0:
                retornaTroco(saldo)
            atualizaStock(stock)
            print("maq: Até à próxima.")
            break
        
        else:
            print("Comando inválido.")

if __name__ == "__main__":
    maquinaVending()


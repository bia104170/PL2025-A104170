from ansintatico import rec_Parser

def main():
    while True:
        try:
            linha = input()
            print(f"Expressão: {linha}")
            print("\n")
        except EOFError:
            break
        if linha.lower() == "sair":
            print("Programa terminado.")
            break
        res = rec_Parser(linha)
        print("\n")
        print(f"O resultado da expressão {linha} é {res}")
        print("----------------------------------------------------------\n")

main()

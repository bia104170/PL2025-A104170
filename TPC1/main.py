def processaTexto(string):
    soma = 0
    ativo = True
    i = 0

    while i < len(string):
        if (string[i:i+3].lower() == 'off'): # passa para minuscula para verificar
            ativo = False
            i += 3 #avança para depois do Off
        elif (string[i:i+2].lower() == 'on'):
            ativo = True
            i += 2
        
        elif(string[i] >= '0' and string[i] <= '9'):
            if ativo:
                numero = ""
                while i < len(string) and string[i] >= '0' and string[i] <= '9':
                    numero = numero + string[i]
                    i += 1
                soma = soma + int(numero)
            else:
                i += 1
                    
        elif string[i] == '=':
            print(f"Resultado da soma: {soma}")
            i += 1

        else:
            i += 1

    return soma
        
def main():
        
    while True:
        
        
        try:
            #Obtem string do input
            string = input()
    
            processaTexto(string)
            
        except EOFError:
            break
        
main()
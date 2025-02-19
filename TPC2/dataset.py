import json

# Abrir o ficheiro CSV
with open("obras.csv", "r", encoding="utf-8") as f:


# Inicializar variáveis
    linha_buffer = ""  # buffer para armazenar a linha
    dataset = []
    separador = ";"  # Separador usado no CSV
    aspas = False  # Para identificar se estamos dentro de um campo entre aspas
    estrutura = {}
    campos_header = []
    j = 0
    n = 0

    for linha in f:

        i = 0

        if j == 0: #header
            campos_header = linha.split(separador)  # Dividir o cabeçalho pelos separadores
            campos_header = [campo.strip() for campo in campos_header]  # Remove o \n
            j += 1

        else:

            while(i < len(linha)):
                char = linha[i]

                if char == '"':
                
                    if aspas and i + 1 < len(linha) and linha[i+1] == '"':
                        linha_buffer += '"'
                        i += 1 #avança para depois da segunda "

                    else:
                        aspas = not aspas # se estiver dentro de aspas mas o proximo char não for "

                elif char == separador and aspas == False: #separador encontrado e fora de aspas
                    estrutura[campos_header[n]] = linha_buffer
                    linha_buffer = ""
                    n += 1

                elif char == '\n' and aspas == False:
                    estrutura[campos_header[n]] = linha_buffer
                    dataset.append(estrutura)
                    n = 0
                    linha_buffer = ""
                    estrutura = {}

                else:
                    linha_buffer += char

                i += 1

    if n != 0:
        estrutura[campos_header[n]] = linha_buffer
        dataset.append(estrutura)

compositores = []
for obra in dataset:
    compositor = obra['compositor']

    if(compositor not in compositores):
        compositores.append(compositor)

compositores_ordenado = sorted(compositores)

print("--------1--------\n")

print(compositores_ordenado)
print('\n')


distribuicao_periodo = {}
for obra in dataset:
    periodo = obra['periodo']

    if periodo in distribuicao_periodo: 
        distribuicao_periodo[periodo] +=  1

    else:
        distribuicao_periodo[periodo] = 1

print("--------2--------\n")

for periodo, quantidade in distribuicao_periodo.items():
   print(f"{periodo}: {quantidade}")
print('\n')

periodo_obras = {}
for obra in dataset:
    periodo = obra['periodo']
    nome = obra['nome']

    if periodo in periodo_obras:
        periodo_obras[periodo].append(nome)
    else:
        periodo_obras[periodo] = [nome]

for periodo in periodo_obras:
    periodo_obras[periodo].sort()

print("--------3--------\n")

for periodo, obras in periodo_obras.items():
    print(f"Período: {periodo}\nTítulos das Obras: {obras}")
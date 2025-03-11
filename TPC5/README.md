# Relatório Trabalho de Casa 5

**Data:** 2025-03-11

## Autor

**Nome:** Beatriz Carvalho Peixoto  
**Número:** A104170  

![Fotografia de identificação](../foto_identificacao.png)

## Resumo
1. Este trabalho de casa consistiu em construir um programa que simula uma máquina de vending.
2. Para a resolução deste trabalho de casa utilizei a biblioteca ply, mais especificamente o ply.lex.
3. Os tokens e as expressões regulares definidas permitiram processar os comandos inseridos como, por exemplo, o "SELECIONAR A23" de modo a ser possível capturar os parâmetros necessários (como o código de um produto) e realizar a ação correspondente. 
3. Esta máquina de vending suporta as seguintes operações:
    - LISTAR que apresenta o lista dos produtos existentes e as suas informações
    - MOEDA que permite inserir o dinheiro
    - SELECIONAR que permite selecionar um dado produto para comprar
    - ADICIONAR que permite adicionar uma dada quantidade de um produto ao stock
    - SAIR que termina a atividade da máquina e salva as suas alterações

## Utilização
Para executar este programa utiliza-se o comando: python3 maquinaVending.py  
Alguns comandos para testar a máquina de vending:
    - LISTAR
    - MOEDA 1e, 50c .
    - SELECIONAR B12
    - ADICIONAR A23 2
    - SAIR

## Lista de Resultados 
Ficheiro onde se encontra o programa em python:
    - ![maquinaVending.py](maquinaVending.py)

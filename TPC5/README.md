# Relatório Trabalho de Casa 5

**Data:** 2025-03-12

## Autor

**Nome:** Beatriz Carvalho Peixoto  
**Número:** A104170  

![Fotografia de identificação](../foto_identificacao.png)

## Resumo
1. Este trabalho de casa consistiu em construir um programa que simula uma máquina de vending.
2. Esta máquina contém um stock de produtos que se encontra no ficheiro json: ![stock.json](stock.json)
3. Os tokens e as expressões regulares definidas permitiram processar os comandos inseridos como, por exemplo, o "SELECIONAR A23" de modo a ser possível capturar os parâmetros necessários (como o código de um produto) e realizar a ação correspondente. 
3. Esta máquina de vending suporta as seguintes operações:
    - LISTAR que apresenta o lista dos produtos existentes e as suas informações
    - MOEDA que permite inserir o dinheiro
    - SELECIONAR que permite selecionar um dado produto para comprar
    - ADICIONAR que permite adicionar uma dada quantidade de um produto ao stock
    - SAIR que termina a atividade da máquina e salva as suas alterações

## Utilização
Para executar este programa utiliza-se o comando: python3 maquinaVending.py  
Os resultados são impressos no terminal.
Alguns comandos para testar a máquina de vending:
1. LISTAR
2. MOEDA 1e, 50c .
3. SELECIONAR B12
4. ADICIONAR A23 2
5. SAIR

## Lista de Resultados 
Na lista abaixo apresenta-se o ficheiro com o programa em python:
- ![Ficheiro com o programa da máquina de vending](maquinaVending.py)

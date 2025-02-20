# Relatório Trabalho de Casa 2

**Data:** 2025-02-19

## Autor

**Nome:** Beatriz Carvalho Peixoto  
**Número:** A104170  

## Resumo
1. Este trabalho de casa consistiu em analisar um dataset sobre obras musicais em csv .  
2. Depois de analisar e processar o ficheiro, foram gerados os resultados para:
    - Uma lista ordenada alfabeticamente dos compositores musicais;
    - A distribuição das obras por período, isto é, quantas obras catalogadas em cada período;
    - Um dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
       desse período;
3. Inicialmente, a ideia para analisar e processar o dataset (obras.csv) era ler cada linha do ficheiro.
4. Contudo, ao analisar o dataset fornecido (obras.csv) para o processar de seguida, verificou-se que na coluna desc do dataset existiam caracteres como o \n que não permitiam a leitura correta de cada linha do dataset. 
5. Assim, foi necessário fazer uma análise mais detalhada, que consistiu em analisar o dataset char a char, garantindo que os caracteres que estavam a dificultar a análise do dataset fossem identificados e tratados de forma correta. Assim:
    - Sempre que era encontrada uma ", verifica-se se essa aspa se encontra dentro de aspas, de modo a ser possível processar corretamente o dataset.
    - Sempre que era encontrado um \n dentro de um campo com aspas, dentro de aspas, este \n era tratado como parte do conteúdo e não como uma quebra de linha.
    - Se for encontrado o separador ; então significa que se analisou o campo todo e pode-se, finalmente, armazená-lo numa estrutura. Essa estrutura é um dicionário que contém todos os campos de uma linha completa do dataset fornecido.
    - Por fim, caso seja encontrado um /n e não se esteja dentro de aspas, é entendido que a leitura de uma linha completa do dataset chegou ao fim e finalmente se adiciona a estrutura completa a uma lista criada para armazenar o dataset analisado.
6. Para gerar os resultados pedidos, os dados foram organizados em estruturas adequadas como listas e dicionários, de modo a facilitar a sua manipulação.
7. Para executar este programa usa-se o comando: python3 dataset.py > output.txt


## Lista de Resultados 
O ficheiro output.txt contém os resultados pedidos.
- ![Ficheiro de output](output.txt)

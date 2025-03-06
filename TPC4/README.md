# Relatório Trabalho de Casa 4

**Data:** 2025-03-06

## Autor

**Nome:** Beatriz Carvalho Peixoto  
**Número:** A104170  

![Fotografia de identificação](../foto_identificacao.png)

## Resumo
1. Este trabalho de casa consistiu em construir um analisador léxico para uma linguagem de query.
2. Para a resolução deste trabalho de casa utilizei a biblioteca ply, mais especificamente o ply.lex, uma vez que pretendia construir um analisador léxico.
3. Este analisador considera os seguintes tokens:
    - SELECT - palavra "select"
    - WHERE - a palavra "where"
    - LIMIT - a palavra "limit"
    - TYPE - o predicado "a"
    - CLASSE - classes como, por exemplo, dbo:MusicalArtist
    - VAR, variáveis como, por exemplo, ?nome
    - STRING, strings dentro da query
    - NUMBER, números inteiros dentro da query
    - POINT, o ponto (.)
    - LBRACE e RBRACE, que correspondem a '{' e '}', respetivamente
    - ID corresponde a identificadores
4. Caracteres não reconhecidos por qualquer expressão regular são considerados erro
5. Neste analisador, espaços brancos e comentários são ignorados

## Utilização
Para executar este programa utiliza-se o comando: python3 analisadorlexico.py < input.txt > output.txt

## Lista de Resultados 
O ficheiro onde se encontra o programa em python é o ficheiro ![analisadorlexico.py](analisadorlexico.py).  
O ficheiro de input (com a query) e o ficheiro output, que contém os resultados, encontram-se na lista abaixo.
- ![Ficheiro de input](input.txt)
- ![Ficheiro de output](output.txt)

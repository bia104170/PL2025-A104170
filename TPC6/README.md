# Relatório Trabalho de Casa 6

**Data:** 2025-03-20

## Autor

**Nome:** Beatriz Carvalho Peixoto  
**Número:** A104170

![Fotografia de identificação](../foto_identificacao.png)

## Resumo
1. Este trabalho de casa consistiu em implementar um programa que calcula o valor de expressões matemáticas. Para o implementar, foi construído um analisador léxico, utilizando a biblioteca ply.lex, e um analisador sintático feito de forma manual.
2. O analisador léxico identifica os tokens necessários que são:
    - NUMBER, que corresponde aos números inteiros
    - OP1, que corresponde aos operadores de '*' e '/'
    - OP2, que corresponde aos operadores de '+' e '-' 
3. O analisador sintático faz o parser dos tokens obtidos da expressão matemática, isto é, analisa a estrutura, a ordem e combinação dos tokens identificados através de uma gramática definida.
4. A gramática definida foi a seguinte:
    - P1: Inicio | EPInicio EN
    - P2: EN | OP2 EPInicio EN
    - P3: €
    - P4: EPInicio | NUMBER EP
    - P5: EP | OP1 NUMBER EP
    - P6: €
5. Esta gramática verifica a organização da expressão e as suas regras de prioridade.
## Utilização
Para utilizar este programa utiliza-se o comando:  python3 main.py < input.txt > output.txt  
Também se pode utilizar através do terminal fazendo: python3 main.py  
Para sair faz-se "sair".

## Lista de Resultados 
Na lista abaixo é apresentado o ficheiro de input, com várias expressões matemáticas, e o ficheiro de output com os resultados.
- ![input.txt](input.txt)
- ![output.txt](output.txt)

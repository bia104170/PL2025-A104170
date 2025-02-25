import re

def conversorTitulo(string):
    res = string
    titulos = re.findall(r"(#{1,})\s+(.+)", string)  

    for num, conteudo in titulos:
        nivel = len(num)  # Conta os #
        html_string = f"<h{nivel}>{conteudo}</h{nivel}>"
        res = re.sub(r"(#{1,})\s+(.+)", html_string, res)
    
    return res

def conversorNegrito(string):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", string)

def conversorItalico(string):
   return re.sub(r"\*(.+?)\*", r"<i>\1</i>", string)

def conversorLinks(string):
    return re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', string)

def conversorImagens(string):
    return re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', string)


def conversorLista(string, dentro_lista=False, tipo_lista=None):

    if re.match(r"^\d+\.\s+(.+)", string):
        if not dentro_lista or tipo_lista != "ol":
            if not dentro_lista:
                abertura = "<ol>\n"
            else:
                abertura = ""
            return abertura + re.sub(r"^\d+\.\s+(.+)", r"  <li>\1</li>", string), True, "ol"
        return re.sub(r"^\d+\.\s+(.+)", r"  <li>\1</li>", string), True, "ol" # se estiver dentro da lista

    elif re.match(r"^[-*]\s+(.+)", string): # lista não ordenada
        if not dentro_lista or tipo_lista != "ul":
            if not dentro_lista:
                abertura = "<ul>\n"
            else:
                abertura = ""
            return abertura + re.sub(r"^[-*]\s+(.+)", r"  <li>\1</li>", string), True, "ul"
        return re.sub(r"^[-*]\s+(.+)", r"  <li>\1</li>", string), True, "ul"

    else:
        if dentro_lista:
            fecharLista = f"\n</{tipo_lista}>"
            return fecharLista + "\n" + string, False, None
        return string, False, None


def processaLinha(string, dentro_lista=False, tipo_lista=None):

    string, dentro_lista, tipo_lista = conversorLista(string, dentro_lista, tipo_lista)
    string = conversorTitulo(string)
    string = conversorNegrito(string)
    string = conversorItalico(string)
    string = conversorImagens(string)
    string = conversorLinks(string)
    return string, dentro_lista, tipo_lista

def main():
    print("<html>\n<body>")
    dentro_lista = False
    tipo_lista = None  # Pode ser "ul" ou "ol"

    while True:
        try:
            string = input() 
            if string.lower() == "exit":  # Para terminar o programa
                break

            s, dentro_lista, tipo_lista = processaLinha(string, dentro_lista, tipo_lista)
            print(s)

        except EOFError:
            break

    if dentro_lista:
        print(f"</{tipo_lista}>")

    print("</body>\n</html>")

if __name__ == "__main__":
    main()
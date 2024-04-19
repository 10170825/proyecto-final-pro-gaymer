"""Métodos para obtener las revistas del archivo csv organizadas de diferentes maneras.
"""

from .csv_utils import read_csv


def get_abc_words_dict() -> dict:
    """Obtiene un diccionario con cada letra y las palabras en los títulos de las revistas que empiecen con ella

    Returns:
        dict: Diccionario con una letra como clave y una lista con palabras que empiezan con esa letra como valor.
    """
    revistas = read_csv()
    titulos = [revista["titulo"].upper() for revista in revistas]
    palabras = []
    for titulo in titulos:
        titulo = titulo.split(" ")
        for palabra in titulo:
            if palabra not in palabras:
                palabras.append(palabra)
    dict_palabras = {}
    for palabra in palabras:
        letra = palabra[0].upper()
        if letra.isalpha():
            if letra not in dict_palabras:
                dict_palabras[letra] = [palabra]
            else:
                dict_palabras[letra].append(palabra)
    dict_palabras = {k: v for k, v in sorted(dict_palabras.items())}
    return dict_palabras


def get_word_journals_dict(dict_palabras: dict, letra: chr) -> dict:
    """Obtiene un diccionario de palabras y las revistas que contienen la palabra en su título.

    Args:
        dict_palabras: Diccionario con cada letra y las palabras que empiezan con esa letra.
        letra: La letra que se quiere buscar en el diccionario de palabras.

    Returns:
        dict: Diccionario con una palabra como clave y una lista de revistas que contienen la palabra en su título como valor.
    """
    revistas = read_csv()
    palabras = dict_palabras[letra.upper()]
    diccionario_revistas = {}
    for palabra in palabras:
        for revista in revistas:
            if palabra in revista["titulo"].upper():
                if palabra not in diccionario_revistas:
                    diccionario_revistas[palabra] = [revista]
                else:
                    diccionario_revistas[palabra].append(revista)
    diccionario_revistas = {k: v for k, v in sorted(diccionario_revistas.items())}
    return diccionario_revistas


if __name__ == "__main__":
    dic = get_abc_words_dict()
    for letra, palabas in dic.items():
        print(f"{letra} - {palabas}")
    revistas_con_palabra = get_word_journals_dict(dic, "b")
    for palabra, revista in revistas_con_palabra.items():
        print(f"{palabra} \n {revista}")
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


def get_word_journals_dict(dict_palabras: dict, letra: str) -> dict:
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
        diccionario_revistas[palabra] = []
        for revista in revistas:
            if palabra in revista["titulo"].upper():
                diccionario_revistas[palabra].append(revista)
    return diccionario_revistas


def get_id_journal_dict() -> dict:
    """Obtiene un diccionario de revistas con sus ids.

    Returns:
        dict: Diccionario con los ids de las revistas como clave y la revista como valor.
    """
    revistas = read_csv()
    dict_ids = {revista["id"]: revista for revista in revistas}
    return dict_ids


def find_journals(palabras: list) -> dict:
    """Obtiene un diccionario de revistas que contienen las palabras buscadas.

    Args:
        palabras: Lista con las palabras que se están buscando.

    Returns:
        list: Lista de revistas cuyo titulo contiene todas las palabras buscadas.
    """
    resultado = []
    revistas = read_csv()
    titulos = {revista["titulo"].upper(): revista for revista in revistas}
    for titulo, revista in titulos.items():
        if all(palabra.upper() in titulo for palabra in palabras):
            resultado.append(revista)
    return resultado


def buscar_revistas_por_palabra(palabra: str):
    """Busca las revistas que contienen la palabra en su título.

    Args:
        palabra (str): Palabra clave para la búsqueda.

    Returns:
        list: Lista de revistas que contienen la palabra en su título.
    """
    revistas = read_csv()
    revistas_encontradas = []
    for revista in revistas:
        if palabra.upper() in revista["titulo"].upper():
            revistas_encontradas.append(revista)
    return revistas_encontradas


if __name__ == "__main__":
    dic = get_abc_words_dict()
    for letra, palabas in dic.items():
        print(f"{letra} - {palabas}")
    revistas_con_palabra = get_word_journals_dict(dic, "b")
    for palabra, revista in revistas_con_palabra.items():
        print(f"{palabra} \n {revista}")

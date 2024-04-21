"""Métodos para escribir y leer archivos CSV
"""

import csv
from os import path
from .Revista import Revista


def write_csv(revista: Revista) -> None:
    """Escribe la información de una revista en un archivo CSV, si no existe el archivo crea uno nuevo.

    Args:
        revista: Objeto revista
    """
    csv_path = "data/revistas.csv"
    csv_path = path.join(path.dirname(__file__), csv_path)
    if not path.isfile(csv_path):
        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(
                [
                    "id",
                    "titulo",
                    "catalogo",
                    "sjr",
                    "q",
                    "total_citas",
                    "url",
                    "subjects",
                    "publisher",
                    "issn",
                    "widget",
                ],
            )
    with open(csv_path, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            [
                revista.id,
                revista.titulo,
                revista.catalogo,
                revista.sjr,
                revista.q,
                revista.total_citas,
                revista.url,
                revista.subjects,
                revista.publisher,
                revista.issn,
                revista.widget,
            ]
        )


def read_csv() -> list:
    """Obtiene un diccionario de revistas con su información a partir del archivo CSV.

    Returns:
        dict: Diccionario con la información de cada revista
    """
    csv_path = "data/revistas.csv"
    csv_path = path.join(path.dirname(__file__), csv_path)
    lista = []
    with open(csv_path, "r", encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista


def revista_in_csv(id: str) -> bool:
    """Revisa si una revista ya se escribio en el archivo csv a partir de su id.

    Args:
        id: Id de una revista (su títutlo sin espacios).

    Returns:
        bool: True si la revista está en el archivo csv y False si no está en el archivo csv.
    """
    csv_path = "data/revistas.csv"
    csv_path = path.join(path.dirname(__file__), csv_path)
    if not path.isfile(csv_path):
        return False
    revistas = [revista["id"] for revista in read_csv()]
    if id in revistas:
        return True
    return False


def urls_in_csv() -> list:
    """Obtiene una lista de urls de revistas ya escritas en el archivo CSV.

    Returns:
        list: Lista con las urls de las revistas que ya se han agregado al CSV.
    """
    csv_path = "data/revistas.csv"
    csv_path = path.join(path.dirname(__file__), csv_path)
    if not path.isfile(csv_path):
        return
    urls = [revista["url"] for revista in read_csv()]
    return urls


if __name__ == "__main__":
    print(revista_in_csv("Cell"))

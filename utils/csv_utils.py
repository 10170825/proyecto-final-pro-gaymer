import csv
from os import path
from Revista import Revista


def write_csv(revista: Revista) -> None:
    csv_path = "data/revistas.csv"
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
                    "total citas",
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
    archivo = "data/revistas.csv"
    lista = []
    with open(archivo, "r", encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista


def revista_in_csv(id: str) -> bool:
    if not path.isfile("data/revistas.csv"):
        return False
    revistas = [revista["id"] for revista in read_csv()]
    if id in revistas:
        return True
    return False


if __name__ == "__main__":
    print(revista_in_csv("Cell"))

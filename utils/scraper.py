"""Métodos para obtener información de las revistas en la página https://www.scimagojr.com
"""

import requests
from bs4 import BeautifulSoup
from .Revista import Revista
from .csv_utils import write_csv, revista_in_csv, urls_in_csv

visited_urls = urls_in_csv()


def paginate_and_write_to_csv() -> None:
    """Maneja la paginación del catálogo de revistas y escribe en el archivo CSV"""
    global visited_urls
    pages = []
    url = "https://www.scimagojr.com/journalrank.php"
    while url:
        if url not in visited_urls:
            write_to_journal_csv(url)
            page = requests.get(url)
            pages.append(page)
            soup = BeautifulSoup(page.text, "html.parser")
            buttons = soup.find(class_="pagination_buttons")
            link = buttons.findAll("a")[1]
            url = link.get("href")
            if url:
                url = f"https://www.scimagojr.com/{url}"
                print(url)
            else:
                break


def get_journal_info(url: str) -> dict:
    """Obtiene la información sobre una revista de su página.

    Args:
        url (str): Enlace a la página de la revista.

    Returns:
        dict: Diccionario con las siguientes claves:
            - 'subjects': Lista con un diccionario que contiene la(s) categoría(s) por cada área  (list).
            - 'publisher': Editorial que publicó la revista (str).
            - 'issn': Lista con número(s) ISSN de la revista. (list).
            - 'widget': Código HTML para insertar un widget con información de la revista. (str).
    """
    global visited_urls
    if url not in visited_urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        grid = soup.find(class_="journalgrid")
        divs = grid.findAll("div")
        i = 0
        subjects = []
        publisher = ""
        issn = []
        for div in divs:
            if i == 1:
                lists = div.find_all("ul", attrs={"class": False})
                for list in lists:
                    area = list.find("a").text.strip()
                    tree = list.find(class_="treecategory")
                    categories = tree.find_all("a")
                    categories = [category.text.strip() for category in categories]
                    subjects.append({area: categories})
            if i == 2:
                publisher = div.find("a").text.strip()
            if i == 5:
                issn = div.find("p").text.split(", ")
            i += 1
        widget = soup.find(id="embed_code").get("value")
        diccionario_info = {
            "subjects": subjects,
            "publisher": publisher,
            "issn": issn,
            "widget": widget,
        }
        return diccionario_info


def write_to_journal_csv(page_url: str) -> None:
    """Crea un objeto Revista y escribe su información en el archivo CSV.

    Args:
        page_url: Enlace de la página de donde se sacarán las revistas.
    """
    page = requests.get(page_url)
    global visited_urls
    soup = BeautifulSoup(page.content, "html.parser")
    thead = soup.find("thead")
    thead.decompose()
    table = soup.find(class_="table_wrap")
    for row in table.find_all("tr"):
        title = row.find(class_="tit")
        title = title.find("a")
        url = title.get("href")
        url = f"https://www.scimagojr.com/{url}"
        if url not in visited_urls:
            title = title.text.strip()
            orde = row.find(class_="orde")
            if orde.text:
                sjr = orde.text.strip()
                sjr = sjr.partition(" ")[0]
            else:
                sjr = 0
            if orde.find("span"):
                q = orde.find("span").text.strip()
            else:
                q = "Sin cuartil"
            columns = row.find_all("td")
            i = 0
            catalogo = ""
            total_citas = 0
            for col in columns:
                if i == 2:
                    catalogo = col.text.strip()
                if i == 9:
                    total_citas = int(col.text.strip())
                i += 1
            info = get_journal_info(url)
            revista = Revista(
                titulo=title,
                catalogo=catalogo,
                sjr=sjr,
                q=q,
                total_citas=total_citas,
                url=url,
                subjects=info["subjects"],
                publisher=info["publisher"],
                issn=info["issn"],
                widget=info["widget"],
            )
            if not revista_in_csv(revista.id):
                write_csv(revista)


if __name__ == "__main__":
    paginate_and_write_to_csv()

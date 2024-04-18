import requests
from bs4 import BeautifulSoup
from Revista import Revista

def get_pages() -> list:
    pages = []
    url = "https://www.scimagojr.com/journalrank.php"
    while url:
        page = requests.get(url)
        pages.append(page)
        soup = BeautifulSoup(page.text, "html.parser")
        buttons = soup.find(class_='pagination_buttons')
        link = buttons.findAll('a')[1]
        url = link.get('href')
        if url:
            url = f"https://www.scimagojr.com/{url}"
        else:
            break
    return pages

def get_journal_info(url):
    dict = {}
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    menu = soup.find(id='mainmenu')
    menu.decompose()
    ul = soup.findAll('ul')
    print(ul)

def get_journals(table):
    revistas = []
    for row in table.find_all('tr'):
        title = row.find(class_='tit')
        title = title.find('a')
        url = title.get('href')
        url = f"https://www.scimagojr.com/{url}"
        title = title.text.strip()
        orde = row.find(class_='orde')
        sjr = orde.text.strip()[0:5]
        q = orde.find('span').text.strip()
        columns = row.find_all('td')
        i=0
        catalogo = ""
        h_index=0
        total_citas = 0
        for col in columns:
            if i ==3:
                catalogo = col.text.strip()
            if i==5:
                h_index = int(col.text.strip())
            if i==9:
                total_citas = int(col.text.strip())
            i+=1
        
        revista = Revista(titulo=title, 
                                catalogo=catalogo, 
                                sjr=sjr, q=q, h_index=h_index, 
                                total_citas=total_citas, url=url)
        revistas.append(revista)
    return revistas

def get_journal_dict(pages) -> dict:
    revistas = []
    for page in pages:
        soup = BeautifulSoup(page.content, 'html.parser')
        thead = soup.find("thead")
        thead.decompose()
        table = soup.find(class_='table_wrap')
        #revistas.extend(lista_revistas(table))

if __name__ == '__main__':
    get_journal_info("https://www.scimagojr.com/journalsearch.php?q=26651&tip=sid&clean=0")
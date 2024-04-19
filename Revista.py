class Revista:
    '''Clase para representar una revista académica y almacenar su información asociada.

    Attributes:
        id: Una cadena que representa la revista.
        titulo: El título de la revista.
        catalogo: El catálogo al que pertenece la revista.
        sjr: El factor de impacto SJR (SCImago Journal Rank) de la revista.
        q: El cuartil al que pertenece la revista.
        total_citas: El número total de citas recibidas por la revista.
        url: Enlace a la pagina de la revista en https://www.scimagojr.com.
        subjects: Lista de diccionarios que contienen el área y categoría de la revista.
        publisher: La editorial que publico la revista.
        issn: Lista de numero(s) ISSN de la revista.
        widget: Código html para insertar un widget con información de la revista.
    '''
    def __init__(self,titulo:str, catalogo:str, sjr:str,
                 q:str, total_citas:str, url:str, 
                 subjects:list[dict[str, str]], publisher:str, issn:list[str], widget:str):
        '''Constructor para la clase Revista
        '''
        self.id = titulo.replace(" ", "")
        self.titulo = titulo
        self.catalogo = catalogo
        self.sjr = float(sjr)
        self.q = q
        self.total_citas = int(total_citas)
        self.url = url
        self.subjects = subjects
        self.publisher = publisher
        self.issn = issn
        self.widget = widget

    def __str__(self) -> str:
        '''Representación en forma de cadena de la instancia de Revista.

        Returns:
            str: Cadena que representa la instancia de Revista en formato CSV.
        '''
        return f'{self.id},{self.titulo},{self.catalogo},{self.sjr},{self.q},{self.total_citas},{self.url},{self.subjects},{self.publisher},{self.issn},{self.widget}'
class Revista:
    def __init__(self,titulo:str,catalogo:str,sjr:str,
                 q:str,h_index:str,total_citas:str, url:str, 
                 subject:str, publisher:str, issn:str, widget:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
        self.sjr = float(sjr)
        self.q = q
        self.h_index = int(h_index)
        self.total_citas = int(total_citas)
        self.url = url
        self.subject = subject
        self.publisher = publisher
        self.issn = issn
        self.widget = widget
    def __str__(self):
        return f'{self.titulo}|{self.catalogos}|{self.sjr}|{self.q}|{self.total_citas}'
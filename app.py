from flask import Flask, render_template
from utils import get_word_journals_dict, get_abc_words_dict

app = Flask(__name__)

diccionario_letras = get_abc_words_dict()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/creditos")
def creditos():
    return render_template("creditos.html")


@app.route("/busqueda/<busqueda>")
def busqueda(busqueda):
    """todavia nose qe hacer con esta"""
    return render_template("busqueda.html")


@app.route("/explorar")
def explorar():
    diccionario_palabras = get_abc_words_dict()
    palabras_letra = [(letra, palabras) for letra, palabras in diccionario_palabras.items()]
    return render_template("explorar.html", palabras_letra=palabras_letra)


@app.route("/explorar/<letra>")
def palabras(letra: str):
    diccionario_palabras = get_abc_words_dict()
    palabras_letra = [(letra, palabras) for letra, palabras in diccionario_palabras.items() if letra == letra.upper()]
    return render_template("explorar.html", palabras_letra=palabras_letra)

@app.route("/explorar/<palabra>")
def revistas_por_palabra(palabra: str):
    diccionario_revistas = get_word_journals_dict(diccionario_letras, palabra[0].upper())
    return render_template("revistas.html", palabra=palabra, revistas=diccionario_revistas.get(palabra.upper(), []))


@app.route("/<id>")
def revista(id: str):
    return render_template("revista.html")

if __name__ == '__main__':
    app.run(debug=True)

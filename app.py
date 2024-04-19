from flask import Flask, render_template
from utils import get_word_journals_dict, get_abc_words_dict

app = Flask(__name__)

diccionario_letras = get_abc_words_dict


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
    return render_template("explorar.html")


@app.route("/explorar/<letra>")
def palabras(letra: str):
    return render_template("palabras.html", palabras=diccionario_letras)


@app.route("/explorar/<palabra>")
def revistas(palabra: str):
    return render_template("revistas.html")


@app.route("/<id>")
def revista(id: str):
    return render_template("revista.html")

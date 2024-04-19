from flask import Flask, render_template
from utils import get_word_journals_dict, get_abc_words_dict

app = Flask(__name__)

diccionario_letras = get_abc_words_dict


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/explorar")
def explorar():
    return render_template("explorar.html", letras=diccionario_letras)

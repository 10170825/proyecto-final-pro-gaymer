from flask import Flask, render_template, request
from utils import (
    get_word_journals_dict,
    get_abc_words_dict,
    get_id_journal_dict,
    find_journals,
)
import json

app = Flask(__name__)

diccionario_letras = get_abc_words_dict()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/creditos")
def creditos():
    return render_template("creditos.html")


@app.route("/busqueda", methods=["GET", "POST"])
def busqueda():
    if request.method == "POST":
        busqueda = request.form.get("busqueda")
        if busqueda:
            revistas = find_journals(busqueda.split(" "))
            return render_template(
                "busqueda.html", busqueda=busqueda, revistas=revistas
            )
    return render_template("busqueda.html")


@app.route("/explorar")
def explorar():
    global diccionario_letras
    letras = diccionario_letras.keys()  # Obtener todas las letras del abecedario
    return render_template("explorar.html", letras=letras)


@app.route("/explorar/<letra>")
def palabras_por_letra(letra: str):
    global diccionario_letras
    palabras = get_abc_words_dict()
    letras = list(diccionario_letras.keys())  # Obtener la lista completa de letras
    return render_template(
        "explorar.html", letra=letra, palabras_letra=palabras[letra], letras=letras
    )


@app.route("/explorar/palabra/<palabra>")
def revistas_por_palabra(palabra: str):
    global diccionario_letras
    revistas = get_word_journals_dict(diccionario_letras, palabra[0])
    return render_template(
        "revistas_por_palabra.html", palabra=palabra, revistas=revistas[palabra]
    )


@app.route("/revista/<id>")
def revista_detalle(id: str):
    dict_revistas = get_id_journal_dict()
    revista = dict_revistas.get(id)
    if revista and 'subjects' in revista:
        subjects_list = json.loads(revista['subjects'].replace("'", '"'))  
        revista['subjects'] = subjects_list  
    return render_template("revista_detalle.html", revista=revista)


if __name__ == "__main__":
    app.run(debug=True)

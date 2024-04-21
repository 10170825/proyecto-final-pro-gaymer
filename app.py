from flask import Flask, render_template, request
from utils import get_word_journals_dict, get_abc_words_dict, get_id_journal_dict, buscar_revistas_por_palabra

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
        palabra_clave = request.form.get("palabra_clave")
        if palabra_clave:
            revistas = buscar_revistas_por_palabra(palabra_clave)
            return render_template("busqueda.html", palabra_clave=palabra_clave, revistas=revistas)
    return render_template("busqueda.html")


@app.route("/explorar")
def explorar():
    diccionario_palabras = get_abc_words_dict()
    letras = diccionario_palabras.keys()  # Obtener todas las letras del abecedario
    return render_template("explorar.html", letras=letras)


@app.route("/explorar/<letra>")
def palabras_por_letra(letra: str):
    diccionario_palabras = get_abc_words_dict()
    palabras_letra = diccionario_palabras.get(letra.upper(), [])
    letras = list(diccionario_palabras.keys())  # Obtener la lista completa de letras
    return render_template("explorar.html", letra=letra, palabras_letra=palabras_letra, letras=letras)

@app.route("/explorar/palabra/<palabra>")
def revistas_por_palabra(palabra: str):
    dict_revistas = get_id_journal_dict()
    revistas = [revista for revista in dict_revistas.values() if palabra.upper() in revista["titulo"].upper()]
    return render_template("revistas_por_palabra.html", palabra=palabra, revistas=revistas)

@app.route("/revista/<id>")
def revista_detalle(id: str):
    dict_revistas = get_id_journal_dict()
    revista = dict_revistas.get(id)
    return render_template("revista_detalle.html", revista=revista)


if __name__ == '__main__':
    app.run(debug=True)

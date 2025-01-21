
from flask import Flask, request, render_template

app = Flask(__name__)
books = []

@app.route('/', methods=['GET'])
def index():
    return render_template("indexx.html")

@app.route('/add_book', methods=['POST'])
def addBook():

    #Recuperation des paralètres
    titre = request.form.get('title')
    auteur = request.form.get('author')
    annee = request.form.get('year')

    books.append(
        {"id": len(books)+1,"title": titre, "author": auteur, "year": annee}
    )
    # Traitement et réponse
    return f'titre: {titre} | auteur : {auteur} | annee : {annee}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




from flask import Flask, request, render_template

app = Flask(__name__)


books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020},
]


@app.route('/', methods=['GET'])
def index():
    return render_template("indexx.html")


@app.route('/search', methods=['GET'])
def search():

    # Récupération du nom de l'auteur depuis les paramètres GET
    authorFromSearch = request.args.get('author')
    exist = False  # Variable pour vérifier si un livre existe ou non

    # Recherche de livres correspondant à l'auteur
    for book in books:
        if book['author'].lower() == authorFromSearch.lower():
            exist = True
            return f"Livre : {book['title']} ({book['year']})"  # Retourne le premier livre trouvé

    # Si aucun livre n'a été trouvé
    if not exist:
        return "Aucun livre trouvé"



    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

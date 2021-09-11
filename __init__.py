from flask import Flask,render_template,request,flash
import requests
import os
app = Flask(__name__)



app.config['SECRET_KEY'] = os.urandom(24)

# Rota inicial,para carregar o template html
@app.route('/')
def indexMeme():
    return render_template('index.html',info="")

@app.route('/GOT',methods=['GET'])
def GOT():
    # category = request.args.get('category')
    nome = request.args.get('nome')
    url = f'https://anapioficeandfire.com/api/characters?name={nome}'
    response = requests.get(url)

    dados = response.json()
    
    if dados == []:
        flash("Nenhum dado encotrado, tente novamente !!!")
        return render_template('index.html',info="")
    casa = dados[0]['allegiances']
    books = dados[0]['povBooks']
    
    lista_casa = []
    lista_livro = []

    for line in books:
        lista_livro.append(requests.get(line).json())
    for line in casa:
        lista_casa.append(requests.get(line).json())
    return render_template('index.html',livros = lista_livro,casas=lista_casa,info=dados[0]) 
    


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True,port=67)
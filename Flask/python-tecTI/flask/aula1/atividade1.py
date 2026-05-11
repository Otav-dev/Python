from flask import Flask


app = Flask(__name__)

@app.route('/')
def ola():
    return 'Olá'
@app.route('/decorator') 
def decorator():
    return 'O padrão de projeto Decorator (decorador ou envoltório) é um padrão estrutural que permite adicionar novos comportamentos ou funcionalidades a um objeto existente em tempo de execução, sem modificar sua estrutura original, nem criar subclasses para cada nova combinação de recursos'
if __name__ == '__main__':
    app.run(debug=True)
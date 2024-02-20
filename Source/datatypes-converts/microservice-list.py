from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/outra', methods=['POST'])
def funcao():
    return jsonify("Parabens mane, descobriu como usar o route")


@app.route('/', methods=['GET'])
def hello_world():
    with open("./Dados/Aluno.json", "r") as arq:
        data = arq.read()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulação de dados de exemplo
    data = {
        'id': 1,
        'name': 'Exemplo',
        'description': 'Hello mundo'
    }

    # Retorna os dados como resposta em formato JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

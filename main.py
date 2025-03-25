from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

url_base = 'http://186.167.69.10:50080/proteoerp/api'

@app.route('/login/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')

    if not user or not password:
        return jsonify({'error': 'Missing user or password'}), 400

    url = f'{url_base}/login/login'
    data = {'user': user, 'password': password}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sinvalub/post/buscar', methods=['POST'])
def search_product():
    token = request.headers.get('Authorization')
    data = request.get_json()

    if not token:
        return jsonify({'error': 'Authorization header is missing'}), 401

    url = f'{url_base}/sinvalub/post/buscar'
    headers = {'Authorization': token}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sinvalub/post/actualizar', methods=['POST'])
def save_new_loc():
    token = request.headers.get('Authorization')
    data = request.get_json()

    if not token:
        return jsonify({'error': 'Authorization header is missing'}), 401

    url = f'{url_base}/sinvalub/post/actualizar'
    headers = {'Authorization': token}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

url_base = 'http://186.167.69.10:50080/proteoerp/api'

@app.route('proteoerp/api/login/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')
    
    if not user or not password:
        return jsonify({'error': 'Missing user or password'}), 400
    
    url = f'{url_base}/login/login'
    data = {'user': user, 'password': password}
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('proteoerp/api/sinvalub/post/buscar', methods=['POST'])
def search_product():
    token = request.headers.get('Authorization')
    data = request.get_json()

    url = f'{url_base}/sinvalub/post/buscar'
    headers = {'Authorization': token} if token else {}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('proteoerp/api/sinvalub/post/actualizar', methods=['POST'])
def save_new_loc():
    token = request.headers.get('Authorization')
    data = request.get_json()

    url = f'{url_base}/sinvalub/post/actualizar'
    headers = {'Authorization': token} if token else {}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # Adjust host and port if needed
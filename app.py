from flask import Flask, request, jsonify

app = Flask(__name__)
latest_string = None

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/submit_string', methods=['POST'])
def submit_string():
    global latest_string
    if 'string' in request.form:
        latest_string = request.form['string']
        response = jsonify({'message': 'String submitted successfully'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify({'error': 'No string found in the request'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 400

@app.route('/get_latest_string', methods=['POST'])
def get_latest_string():
    global latest_string
    if latest_string is not None:
        return jsonify({'latest_string': latest_string})
    else:
        return jsonify({'error': 'No string available'}), 404

if __name__ == '__main__':
    app.run(debug=True)

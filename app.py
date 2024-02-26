from flask import Flask, request, jsonify

app = Flask(__name__)
latest_string = None

@app.route('/submit_string', methods=['POST'])
def submit_string():
    global latest_string
    if 'string' in request.form:
        latest_string = request.form['string']
        return jsonify({'message': 'String submitted successfully'})
    else:
        return jsonify({'error': 'No string found in the request'}), 400

@app.route('/get_latest_string', methods=['POST'])
def get_latest_string():
    global latest_string
    if latest_string is not None:
        return jsonify({'latest_string': latest_string})
    else:
        return jsonify({'error': 'No string available'}), 404

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

from sport import sport

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/sport')
def getProducts():
    return jsonify({'sport': sport})


@app.route('/sport/<string:sport_name>')
def getProduct(sport_name):
    sportFound = [
        sport for sport in sport if sport['name'] == sport_name.lower()]
    if (len(sportFound) > 0):
        return jsonify({'sport': sportFound[0]})
    return jsonify({'message': 'Sport Not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)

from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from bayesian_multi_classifier import Predict
DATADIR = './categories/'
predictor = Predict(DATADIR)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/categories')
def categories():
    return jsonify({'categories': predictor.categories})


@app.route('/classify', methods=['POST'])
@cross_origin()
def classify():
    data = request.json
    now = datetime.now().isoformat()
    if data['keimeno'] == '':
        return jsonify({'predicted': ''})
    return jsonify({'predicted': predictor.predict_one(data['keimeno'])})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

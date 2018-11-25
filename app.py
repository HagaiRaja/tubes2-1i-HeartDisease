from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import json
import dataprocessing

# melakukan load model
model = joblib.load('model/nb_model.sav')

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def get_delay():
    result=request.form
    # melakukan proses input
    user_input = dataprocessing.collectData(result)
    # mendapatkan prediksi
    heart_disease_pred = model.predict(user_input)
    # return prediksi
    return json.dumps({'predict':heart_disease_pred});

if __name__ == '__main__':
    app.run(port=8080, debug=True)
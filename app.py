from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import json
import dataprocessing

# melakukan load model
model = joblib.load('model/nb_model.sav')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_form():
    return render_template('index.html')

@app.route('/api', methods=['GET', 'POST'])
def get_delay():
    result=request.form
    # melakukan proses input
    user_input = dataprocessing.collectData(result)
    # mendapatkan prediksi
    print(user_input.head())
    #for i in user_input:
     #   print(i, user_input[i])

    heart_disease_pred = model.predict(user_input)
    # return prediksi
    return(json.dumps({'predict':int(heart_disease_pred[0])}))

if __name__ == '__main__':
    app.run(port=8081, debug=True)

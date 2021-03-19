from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method=='POST':
        gre=request.form["gre"]
        toefl=request.form["toefl"]
        university_rating=request.form["university_rating"]
        statement_of_purpose=request.form["statement_of_purpose"]
        letter_of_recommendation=request.form["letter_of_recommendation"]
        cgpa=request.form["cgpa"]
        research=request.form["research"]

    input_variables = pd.DataFrame([[gre, toefl, university_rating, statement_of_purpose, letter_of_recommendation, cgpa, research]], columns=['gre', 'toefl', 'university_rating', 'statement_of_purpose', 'letter_of_recommendation', 'cgpa', 'research'], dtype='float', index=['input'])

    predictions = model.predict(input_variables)[0]

    return render_template('index.html', original_input={'GRE':gre, 'TOEFL':toefl, 'University Rating':university_rating, 'Statement of Purpose':statement_of_purpose, 'Letter of Recommendation':letter_of_recommendation, 'CGPA':cgpa, 'Research':research}, result=predictions)



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    predictions = model.predict([np.array(list(data.values()))])

    output = predictions[0]
    return jsonify(output)



if __name__ == "__main__":
    app.run(port=5000,debug=True)
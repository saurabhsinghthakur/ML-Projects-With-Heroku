import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model-glass.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''


    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction[0] == 1:
    	glass_type = "Building Windows 1"
    elif prediction[0] == 2:
    	glass_type = "Building Windows 2"
    elif prediction[0] == 3:
    	glass_type = "Vehicle Windows 1"
    elif prediction[0] == 4:
    	glass_type = "Vehicle Windows 2"
    elif prediction[0] == 5:
    	glass_type = "Containers"
    elif prediction[0] == 6:
    	glass_type = "TableWare"
    elif prediction[0] == 7:
    	glass_type = "Headlamps"
    else:
    	glass_type = "Sorry! Input Not Valid"

    return render_template('index.html', prediction_text='Glass Type: {}'.format(glass_type))

if __name__ == "__main__":
    app.run(debug=True)


#1.51685	14.92	0.0	1.99	73.06	0.00	8.40	1.59	0.0
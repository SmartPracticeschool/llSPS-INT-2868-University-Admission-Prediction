import numpy as np
from flask import Flask,request ,jsonify ,render_template
import pickle
import sklearn
from werkzeug.debug import console



app = Flask(__name__)

model = pickle.load(open('randomforest.h5' , 'rb'))

@app.route('/')
def home():
    return render_template('Demo2.html')

@app.route('/y_predict' ,methods = ['POST'])
def y_predict():

  x_test =[[float(x) for x in request.form.values()]]

  prediction = model.predict(x_test)
  print(prediction)
  output=prediction[0][0]
  return render_template('Demo2.html', prediction_text='Probability of admission {}'.format(output))

if __name__ == "__main__":
   app.run(debug=True)
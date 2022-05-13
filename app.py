from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def index():
    data1 = request.form['gender']
    data2 = request.form['age']
    data3 = request.form['exercise_importance']
    data4 = request.form['regularity']
    data5 = request.form['b_1']
    data6 = request.form['b_2']
    data7 = request.form['b_3']
    data8 = request.form['b_4']
    data9 = request.form['b_5']
    data10 = request.form['b_6']
    data11 = request.form['b_other']
    data12 = request.form['e_1']
    data13 = request.form['e_2']
    data14 = request.form['e_3']
    data15 = request.form['e_4']
    data16 = request.form['e_5']
    data17 = request.form['e_6']
    data18 = request.form['e_7']
    data19 = request.form['e_8']
    data20 = request.form['e_other']
    data21 = request.form['do_you']
    data22 = request.form['time']
    data23 = request.form['time_spent']
    data24 = request.form['balanced_diet']  
    data25 = request.form['pb_1']
    data26 = request.form['pb_2']
    data27 = request.form['pb_3']
    data28 = request.form['pb_4']
    data29 = request.form['pb_5']
    data30 = request.form['pb_other']
    data31 = request.form['health_level']
    data32 = request.form['recommend_fitness']
    data33 = request.form['equipment']
    data34 = request.form['m_1']
    data35 = request.form['m_2']
    data36 = request.form['m_3']
    data37 = request.form['m_4']
    data38 = request.form['m_5']
    data39 = request.form['m_6']
    data40 = request.form['m_7']
    data41 = request.form['m_other']

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26, data27, data28, data29, data30, data31, data32, data33, data34, data35, data36, data37, data38, data39, data40, data41]])
    print (arr)
    pred = model.predict(arr)
    print (pred)
    return render_template('predict.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
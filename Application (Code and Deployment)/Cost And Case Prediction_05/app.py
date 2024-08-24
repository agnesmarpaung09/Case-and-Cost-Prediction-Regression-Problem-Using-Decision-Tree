from flask import Flask, request, render_template
import pickle

import numpy

app = Flask(__name__)

model_file1 = open('modelcost.pkl', 'rb')
model1 = pickle.load(model_file1, encoding='bytes')

model_file2 = open('modelcase.pkl', 'rb')
model2 = pickle.load(model_file2, encoding='bytes')


@app.route("/", methods=['GET'])
def indexku():
    return render_template("index.html")


@app.route("/case")
def case():
    return render_template("case.html")


@app.route("/cost")
def cost():
    return render_template("cost.html")

# @app.route("case/predict", methods=["POST"])
# def cost_predict():
#     if request.method == 'POST':
#         kddati2 = float(request.form['kddati2'])
#         tkp = float(request.form['tkp'])
#         peserta = float(request.form['peserta'])
#         rs = float(request.form['rs'])
#         cost = float(request.form['cost'])
#         return render_template("case.html")
#     else:
#         return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

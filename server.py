from flask import Flask, request, jsonify, redirect, Response, json, render_template
import os
import pprint

app = Flask(__name__)

@app.route("/")
def show_index():
    return render_template('index.html')


@app.route("/analyze", methods=["POST"])
def analyze():
    woes = request.form['woes']
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)

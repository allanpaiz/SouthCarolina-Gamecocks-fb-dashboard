from flask import Flask, render_template
import plotly.express as px
from flask import jsonify
from data.hp_1 import create_main_scatter


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chart-data')
def chart_data():
    chart = create_main_scatter()
    return jsonify(chart)

if __name__ == '__main__':
    app.run(debug=True)
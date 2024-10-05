from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, template_folder='docs')

# Load the CSV data
data_path = os.path.join(os.getcwd(), 'data', 'Yojana info.csv')
data = pd.read_csv(data_path)

# Define sectors
sectors = data['Sector'].unique()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        sector = request.form['sector']
        filtered_data = data[data['Sector'] == sector]
        return render_template('results.html', name=name, data=filtered_data.to_dict(orient='records'))
    return render_template('index.html', sectors=sectors)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

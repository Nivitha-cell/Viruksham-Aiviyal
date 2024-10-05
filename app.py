
from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, template_folder='docs')

# Load the CSV data
data_path = os.path.join(os.getcwd(), 'data', 'Yojana info.csv')
data = pd.read_csv(data_path)

# Define sectors and schemes
sectors = data['Sector'].unique()
schemes = data[['Sector', 'Yojana Name', 'Eligibility', 'Deadline', 'Benefits']]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        sector = request.form['sector']
        filtered_schemes = schemes[schemes['Sector'] == sector]
        return render_template('results.html', name=name, schemes=filtered_schemes.to_dict(orient='records'))
    return render_template('index.html', sectors=sectors)

if __name__ == '__main__':
    app.run(debug=True, port=5001)


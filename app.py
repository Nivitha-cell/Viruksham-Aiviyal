from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load data from the CSV file
file_path = r'D:\WomenEmpowermentApp\data\yojana info.csv'
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    print("File not found.")

@app.route('/')
def index():
    # Get unique sectors for the dropdown list
    sectors = data['Sector'].unique()
    return render_template('index.html', sectors=sectors)

@app.route('/check', methods=['POST'])
def check():
    name = request.form['name']
    sector = request.form['sector']
    
    # Filtering logic based on selected sector
    eligible_schemes = data[data['Sector'].str.lower() == sector.lower()]

    return render_template('results.html', name=name, schemes=eligible_schemes.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

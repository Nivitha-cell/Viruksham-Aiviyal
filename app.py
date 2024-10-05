from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Specify the path to the yojana data
file_path = 'data/Yojana info.csv'  # Adjusted the path to point to the 'data' folder

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")

# Load the yojana data from the CSV file
yojana_data = pd.read_csv(file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    name = request.form.get('name')
    sector = request.form.get('sector')

    # Filter the yojanas based on the selected sector
    eligible_schemes = yojana_data[yojana_data['Sector'] == sector]

    schemes = []
    for _, row in eligible_schemes.iterrows():
        schemes.append({
            'Name': row['Yojana Name'],
            'Sector': row['Sector'],
            'Description': row['Eligibility'],
            'Benefits': row['Benefits'],
        })

    return render_template('results.html', schemes=schemes, name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

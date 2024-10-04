from flask import Flask, render_template, request
import pandas as pd
import os

# Set the template folder to 'docs'
app = Flask(__name__, template_folder='docs')

# Load data from the CSV file
file_path = r'D:\WomenEmpowermentApp\data\yojana info.csv'
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    print("File not found.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    age = int(request.form['age'])
    employment_status = request.form['employment_status']
    sector = request.form['sector']
    
    # Filtering logic based on user input
    eligible_schemes = data[
        (data['Age Requirement'] <= age) &
        (data['Employment Status'].str.lower() == employment_status.lower()) &
        (data['Sector'].str.lower() == sector.lower())
    ]

    return render_template('results.html', schemes=eligible_schemes.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

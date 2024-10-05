from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, template_folder='docs')

# Load the CSV data
data_path = 'data/Yojana info.csv'  # Adjust path if necessary
data = pd.read_csv(data_path)
print("CSV file loaded successfully.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    selected_sector = request.form['sector']
    
    # Filter the data based on the selected sector
    filtered_data = data[data['Sector'] == selected_sector]

    return render_template('results.html', data=filtered_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use port 5001

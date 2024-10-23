from flask import Flask, render_template, request, redirect
import pandas as pd
import os
import sqlite3

app = Flask(__name__, template_folder='docs')

# Load the CSV data for yojanas
data_path = os.path.join(os.getcwd(), 'data', 'Yojana info.csv')
data = pd.read_csv(data_path)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT NOT NULL,
            sector TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database on startup
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        sector = request.form['sector']

        # Save the user data into the database
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, contact, sector) VALUES (?, ?, ?)
        ''', (name, contact, sector))
        conn.commit()
        conn.close()

        # Filter yojanas based on the selected sector
        filtered_data = data[data['Sector'] == sector]
        return render_template('results.html', name=name, data=filtered_data.to_dict(orient='records'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

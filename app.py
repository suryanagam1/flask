from flask import Flask, render_template, jsonify,request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def db_conn():
    conn = psycopg2.connect(database="postgres", host="localhost", user="postgres", password="123456", port="5432")
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/folders', methods=['GET'])
def get_folders():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT datasets FROM Data')  # Adjust the query as needed
    folders = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(folders)


@app.route('/api/data/', methods=['GET'])
def get_data():
    folder_name = request.args.get('folder')
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Data WHERE datasets = %s''', (folder_name,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    
    # Convert the fetched data into a list of dictionaries
    data_list = [{'datasets': row[1], 'category': row[2], 'free': row[3], 'rating': row[4], 'description': row[5]} for row in data]
    return jsonify(data_list)

if __name__ == "__main__":
    app.run(debug=True)

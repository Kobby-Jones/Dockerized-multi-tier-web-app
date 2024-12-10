# backend/app.py
from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

db_connection = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME')
)

cursor = db_connection.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT 'Hello form the database'")
    result = cursor.fetchone()
    return jsonify({'message': result[0]})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

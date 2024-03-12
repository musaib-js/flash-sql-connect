from flask import Flask, jsonify
from sqlalchemy import create_engine
import urllib.parse


app = Flask(__name__)

connection_string = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=master;Trusted_Connection=yes;')
engine = create_engine(connection_string)


@app.route('/')
def hello_world():
    return 'Hello, Musaib. We`re up!'

@app.route('/connect')
def connect():
    try:
        with engine.connect():
            return jsonify(status='Connected to the database')
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run()
    
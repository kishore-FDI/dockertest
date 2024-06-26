from flask import Flask,jsonify
from waitress import serve
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app=Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'content':"Server is running on kishore PC"
    })
if __name__ == '__main__':
    serve(app,host='0.0.0.0',port='50100',threads=1,url_prefix='/my-pc')
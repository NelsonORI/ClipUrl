from flask import Flask, jsonify 
from config import create_app

app = create_app()

@app.route('/',methods=['GET'])
def home():
    return jsonify({'message':'Server working'})

if __name__ == '__main__':
    app.run(port=5555,debug=True)
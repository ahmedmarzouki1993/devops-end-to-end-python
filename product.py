from flask import Flask
app = Flask(__name__)

@app.route('/') 
def product():
    return 'Hello, World! from product'     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
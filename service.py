from flask import Flask

app = Flask('__main__')

@app.route('/')
def service():
    return 'Hello, World! from service' 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
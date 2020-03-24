from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    print("root")
    message = "Hello template"
    return render_template('index.html', message=message)

@app.route('/json')
def json(): 
    print("json path")
    result = {}
    result["hello"] = "world"
    return jsonify(result)

if __name__ == '__main__':
    app.run()

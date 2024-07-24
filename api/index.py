from flask import Flask, jsonify, request


app = Flask(__name__)


# Route served as a static page
@app.route('/')
def home():
    return 'Hellooooo'


# Route with method served as JSON API
@app.route('/product', methods=['GET'])
def product():
    url = request.url
    return jsonify({
        'get-request-served-from' : url
    })


# Running debugger in console
if __name__ == '__main__':
    app.run(debug=True)
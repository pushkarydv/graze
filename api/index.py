from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    'items': []
}

@app.route('/')
def home():
    return 'Hellooooo'

@app.route('/product', methods=['GET'])
def product():
    url = request.url
    return jsonify({
        'get-request-served-from' : url
    })

# if __name__ == '__main__':
#     app.run(debug=True)
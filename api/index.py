from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


# Route served as a static page
@app.route('/')
def home():
    return render_template('index.html')


productData =  {
    '1': {
        'name': 'Product 1',
        'price': 100,
    },
    '2': {
        'name': 'Product 2',
        'price': 200
    },
    '3': {
        'name': 'Product 3',
        'price': 300
    },
    '4': {
        'name': 'Product 4',
        'price': 400
    },
}

coupons = {
    'early-max': 50,
    'flask40': 40,
    'flask20': 20
}

def get_product(id):
    return productData[str(id)] if str(id) in productData else 'Product not found'  

# discount from coupon else <int> 0 
def get_discount(coupon):
    return coupons[coupon] if coupon in coupons else 0


def product(id):
    coupon = request.args.get('coupon', 'No Coupon Applied')
    try:
        return {
            'product_id': id,
            'product_name': get_product(id),
            'coupon': coupon,
            'discount': get_discount(coupon),
            'price': get_product(id)['price'] / 100 * (100 - get_discount(coupon))
        }
    except Exception as e:
        return {
            'error': str(e)
        }

@app.route('/product/<int:id>')
def product_page(id):
    
    if id not in productData:
        return render_template('product.html')
    
    return render_template('product.html', product=product(id))

# Running debugger in console
if __name__ == '__main__':
    app.run(debug=True)
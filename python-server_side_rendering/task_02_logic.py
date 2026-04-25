from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = load_json()
    elif source == 'csv':
        data = load_csv()
    elif source == 'sql':
        data = load_sqlite()
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    if data is None:
        return render_template('product_display.html',
                               error="Error loading data")

    # ✅ HANDLE ID FILTERING
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p["id"] == product_id]

            if not filtered:
                return render_template('product_display.html',
                                       error="Product not found")

            data = filtered

        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html',
                           products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
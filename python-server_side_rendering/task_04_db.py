from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON error: {e}")
        return []

# CSV
def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        print(f"CSV error: {e}")
    return products

# SQLite
def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Load data
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        data = read_sql()

    # Filter by ID
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template(
                    'product_display.html',
                    error="Product not found",
                    products=[]
                )
        except ValueError:
            return render_template(
                'product_display.html',
                error="Invalid ID format",
                products=[]
            )

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
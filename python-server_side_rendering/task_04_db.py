#!/usr/bin/python3
import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Only insert if table is empty to avoid duplicate data on restart
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
    conn.close()


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            row['id'] = int(row['id'])
            products.append(row)
    return products


def read_sql(product_id=None):
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    if product_id is not None:
        cursor.execute(
            'SELECT id, name, category, price FROM Products WHERE id = ?',
            (product_id,)
        )
    else:
        cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    try:
        if source == 'json':
            products_data = read_json()
        elif source == 'csv':
            products_data = read_csv()
        elif source == 'sql':
            products_data = read_sql(product_id)
        else:
            return render_template('product_display.html', error="Wrong source")
    except sqlite3.Error as e:
        return render_template('product_display.html',
                               error=f"Database error: {str(e)}")
    except FileNotFoundError as e:
        return render_template('product_display.html',
                               error=f"File not found: {str(e)}")
    except Exception as e:
        return render_template('product_display.html',
                               error=f"Error: {str(e)}")

    # Filter by id for json/csv sources too
    if product_id is not None and source in ('json', 'csv'):
        products_data = [p for p in products_data if int(p.get('id', -1)) == product_id]

    if product_id is not None and not products_data:
        return render_template('product_display.html',
                               error="Product not found")

    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
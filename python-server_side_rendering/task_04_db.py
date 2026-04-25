#!/usr/bin/python3
"""
Task 4 - Flask app with JSON, CSV, and SQLite support
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def load_json():
    """Load products from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return None


def load_csv():
    """Load products from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None


def load_sqlite():
    """Load products from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except Exception:
        return None



@app.route('/products')
def products():
    source = request.args.get('source')

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

    return render_template('product_display.html',
                           products=data)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
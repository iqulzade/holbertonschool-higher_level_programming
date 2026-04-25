import sqlite3
import os

def create_database():
    # Remove corrupted DB if it exists
    if os.path.exists('products.db'):
        try:
            os.remove('products.db')
        except Exception as e:
            print(f"Error removing old DB: {e}")

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    cursor.executemany('''
        INSERT INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
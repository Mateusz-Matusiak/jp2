import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO store (product_name, quantity, product_details) VALUES (?, ?, ?)",
            ('Ball', 300, 'Basket ball')
            )

cur.execute("INSERT INTO store (product_name, quantity, product_details) VALUES (?, ?, ?)",
            ('Armchair',400, 'Very comfortable airmchair')
)

connection.commit()
connection.close()
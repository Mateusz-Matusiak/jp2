DROP TABLE IF EXISTS posts;

CREATE TABLE store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    product_details TEXT NOT NULL
);

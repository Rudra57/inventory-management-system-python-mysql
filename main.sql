CREATE DATABASE inventory_db;
USE inventory_db;
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price  DECIMAL(10,2) NOT NULL
);
SHOW TABLES;
INSERT INTO products (product_name, quantity, price)
VALUES ('Mouse', 50, 12.99);
SELECT * FROM products;
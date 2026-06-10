import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tanukutti@1996",
    database="inventory_db"
)

cursor = conn.cursor()


def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    sql = "INSERT INTO products (product_name, quantity, price) VALUES (%s, %s, %s)"
    values = (name, quantity, price)

    cursor.execute(sql, values)
    conn.commit()

    print("Product added successfully!\n")


def view_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nID | Name | Quantity | Price")
    print("-" * 35)

    for product in products:
        id, name, quantity, price = product
        print(f"{id} | {name} | {quantity} | {price} euro")

    print()


while True:
    print("===== INVENTORY MENU =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")


cursor.close()
conn.close()
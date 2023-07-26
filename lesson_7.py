import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(conn, products):
    sql = '''INSERT INTO PRODUCTS
    (product_tittle, price, quantity)
    VALUES (?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity_by_id(conn, product_id, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_quantity, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price_by_id(conn, product_id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_price, product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product_by_id(conn, product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_cheap_products(conn):
    sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_product_by_tittle(conn, search_tittle):
    sql = '''SELECT * FROM products WHERE product_tittle LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + search_tittle + '%',))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_tittle VARCHAR(200) NOT NULL,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')
    create_table(connection_to_db, sql_create_products_table)
    insert_products(connection_to_db, ('мыло', 104.57, 2))
    insert_products(connection_to_db, ('шампунь', 50, 1))
    insert_products(connection_to_db, ('бальзам', 56, 1))
    insert_products(connection_to_db, ('гель', 9, 1))
    insert_products(connection_to_db, ('ведро', 30, 1))
    insert_products(connection_to_db, ('щетка', 4, 2))
    insert_products(connection_to_db, ('метла', 20, 2))
    insert_products(connection_to_db, ('порошок', 50, 2))
    insert_products(connection_to_db, ('резинка', 15, 15))
    insert_products(connection_to_db, ('лак', 4, 6))
    insert_products(connection_to_db, ('тряпка', 35, 2))
    insert_products(connection_to_db, ('хлор', 5, 2))
    insert_products(connection_to_db, ('сода', 7, 2))
    insert_products(connection_to_db, ('пакет', 47, 3))
    insert_products(connection_to_db, ('детское мыло', 34, 2))
    select_all_products(connection_to_db)
    update_quantity_by_id(connection_to_db, 1, 15)
    update_price_by_id(connection_to_db, 1, 30)
    delete_product_by_id(connection_to_db, 2)
    select_cheap_products(connection_to_db)
    search_product_by_tittle(connection_to_db, "мыло")

    connection_to_db.close()

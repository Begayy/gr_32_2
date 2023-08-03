import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def get_employees_by_city(conn, city_id):
    sql = '''SELECT e.first_name, e.last_name, co.title, ci.title, ci.area
                      FROM employees AS e
                      LEFT JOIN cities AS ci ON e.city_id = ci.id
                      LEFT JOIN countries AS co ON ci.country_id = co.id
                      WHERE e.city_id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (city_id,))
        row_list = cursor.fetchall()
        for row in row_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def main(conn):
    sql = '''SELECT id, title FROM cities'''

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        print("Вы можете отобразить список сотрудников по выбранному "
              "id города из перечня городов ниже, для выхода из программы введите 0:")

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(f"{row[0]}. {row[1]}")
        input_city_id = int(input("Введите id города: "))

        if input_city_id == 0:
            print("Программа завершена.")
        elif input_city_id == get_employees_by_city(connection_to_db, input_city_id):
            for employee in rows_list:
                print(
                    f"Имя: {employee[0]}, Фамилия: {employee[1]}, Страна: {employee[2]}, Город: {employee[3]}, Площадь города: {employee[4]}")

    except sqlite3.Error as e:
        print(e)


connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')
    main(connection_to_db)
    connection_to_db.close()

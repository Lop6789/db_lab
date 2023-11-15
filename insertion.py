from databased import *

def settings_insertion(connection, qty = 100):
    with connection.cursor() as cursor:
        for i in range(qty):
            inp = generate_settings()
            cursor.execute(
                f"INSERT INTO \"Settings\" (settings_id, version, language, other_settings) "
                f"VALUES ({inp[0]}, {inp[1]}, \'{inp[2]}\', {inp[3]})"
            )
        print("[INFO] Data was succefully inserted")

def category_insertion(connection, qty = 8):
    with connection.cursor() as cursor:
        inp = generate_category()
        for i in range(qty):
            cursor.execute(
                f"INSERT INTO \"Category\" (category_id, name) "
                f"VALUES ({i + 1}, \'{inp[i]}\')"
            )
        print("[INFO] Data was succefully inserted")

def list_insertion(connection, qty = 70):
    with connection.cursor() as cursor:
        for i in range(qty):
            inp = generate_list()
            cursor.execute(
                f"INSERT INTO \"List\" (list_id, name) "
                f"VALUES ({inp[0]}, \'{inp[1]}\')"
            )
        print("[INFO] Data was succefully inserted")

        

def product_insertion(connection, qty = 250):
    with connection.cursor() as cursor:
        for i in range(qty):
            inp = generate_product()
            cursor.execute(
                f"INSERT INTO Product (product_id, name, colour, quantity, status) "
                f"VALUES ({inp[0]}, \'{inp[1]}\', \'{inp[2]}\', {inp[3]}, \'{inp[4]}\')"
            )
        print("[INFO] Data was succefully inserted")


def list_product_insertion(connection, qty = 50):
    with connection.cursor() as cursor:
        for i in range(qty):
            inp = generate_list_product()
            cursor.execute(
                f"INSERT INTO List_Product (list_product_id, product_id, list_id) "
                f"VALUES ({inp[0]}, {inp[1]}, {inp[2]})"
            )
        print("[INFO] Data was succefully inserted")


def product_category_insertion(connection, qty = 200):
    with connection.cursor() as cursor:
        for i in range(qty):
            cursor.execute(
                f"INSERT INTO Product_Category (product_category_id, product_id, category_id) "
                f"VALUES ({i + 1}, {random.randint(1, product_id)}, {random.randint(1, 8)})"
            )
        print("[INFO] Data was succefully inserted")

def user_insertion(connection, qty = 100):
    with connection.cursor() as cursor:
        for i in range(qty):
            inp = generate_user()
            cursor.execute(
                f"INSERT INTO \"User\" (user_id, email, login, settings_id, password) "
                f"VALUES ({inp[0]}, \'{inp[1]}\', \'{inp[2]}\', {inp[3]}, \'{inp[4]}\')"
            )
    print("[INFO] Data was succefully inserted")


def user_list_insertion(connection, qty = 100):
    with connection.cursor() as cursor:
        for i in range(1, list_id):
            cursor.execute(
                f"INSERT INTO user_list (user_list_id, user_id, list_id) "
                f"VALUES ({i}, {random.randrange(1, id)}, {random.randrange(1, list_id)})"
            )
    print("[INFO] Data was succefully inserted")



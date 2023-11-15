import psycopg2
from insertion import *
from databased import *
from config import host, user, password, db_name


try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True

    settings_insertion(connection)
    user_insertion(connection)
    list_insertion(connection)
    product_insertion(connection)
    category_insertion(connection)
    user_list_insertion(connection)
    list_product_insertion(connection)
    product_category_insertion(connection)


    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
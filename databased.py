import random
import string  # импортирую для генерации пароля
import json
id = 1
settings_id = 1
list_id = 1
product_id = 1
list_product_id = 1

def generate_settings():
    settings = []
    global settings_id
    settings.append(settings_id)
    settings_id += 1
    version = 2023
    language = generate_language()
    other_settings = random.randint(0, 1)
    settings.append(version)
    settings.append(language)
    settings.append(other_settings)
    return settings



def generate_user():
    user = []
    login = generate_login()
    global id
    user.append(id)
    id += 1
    user.append(generate_mail(login))
    user.append(login)
    user.append(id - 1)
    user.append(generate_password())
    return user

# def generate_list():
#     list = []
#     for i in range(1, random.randint(1, 10) + 1):
#         list.append(random.choice(LIST_NAME) + str(random.randint(1, 100)))
#     return list

def generate_list():
    list = []
    global list_id
    list.append(list_id)
    list_id += 1
    list.append(random.choice(LIST_NAME))
    return list

def generate_product():
    product = []
    global product_id
    product.append(product_id)
    product_id += 1
    product.append(random.choice(PRODUCT))
    product.append(random.choice(COLOURS))
    product.append(random.randint(1, 10))
    product.append(random.choice(["Bought", "Not bought"]))
    return product

def generate_list_product():
    list_product = []
    global list_product_id
    list_product.append(list_product_id)
    list_product_id += 1

    global product_id
    global list_id
    list_product.append(random.randrange(1, product_id))
    list_product.append(random.randrange(1, list_id))
    return list_product
    

def generate_category():
    category_list = []
    for i in range(8):
        category_list.append(CATEGORY_NAME[i])
    return category_list
    
    # list = []
    # for i in range(random.randint(1,6)):
    #     list.append(random.choice(CATEGORY_NAME))
    # return list

def generate_password():
    characters = string.ascii_letters + string.digits + '!"#$%&()*+,-./:;<=>?@[\]^_{|}~'
    password = ''.join(random.choice(characters) for _ in range(random.randint(1, 60)))

    return password

def generate_login():
    login = random.choice(NAME) + random.choice(LAST_NAME) + str(random.randint(1, 10000))
    return login

def generate_mail(login):
    mail = login + "@" + random.choice(MAIL)
    return mail

def generate_colour():
    return random.choice(COLOURS)

# def generate_product():
#     product =[]
#     for i in range(random.randint(1, 20)):
#         product.append(random.choice(PRODUCT))
#     return product

def generate_language():
    language = random.choice(["Russia", "English"])
    return language

CATEGORY_NAME = [
    "tech",
    "dairy",
    "books",
    "meat",
    "fruit",
    "drink",
    "veges",
    "fish"
]
LIST_NAME = [
    "home",
    "dinner",
    "party",
    "fishing",
    "funeral",
    "daily",
    "tech",
    "wedding",
    "date",
    "IMPORTANT",
    "wish",
    "trip",
    "urgent"
]
PRODUCT = [
    "bacon",
    "beef",
    "chicken",
    "ham",
    "pork",
"cod",
    "trout",
    "sole",
    "pike",
    "eel",
"chick peat",
    "beet",
    "broccoli",
    "carrot",
    "cucumber",
    "eggplant",
    "egg",
    "pea",
    "potato",
    "garlic",
    "LEEK",
    "apple",
    "banane",
    "cherry",
    "cranberry",
    "grape",
    "plum",
    "pineapple",
    "pear",
    "grain"
    "rice",
    "semolina",
    "buckwheat",
    "wheat",
    "butter",
    "cheeae",
    "cream",
    "cottage cheese",
    "ice cream",
    "coffee",
    "juice",
    "soda",
    "sugar",
    "pancake",
    "muffin",
    "marmalade",
    "vanila"
]
MEAT = [
    "bacon",
    "beef",
    "chicken",
    "ham",
    "pork"
]
FISH =[
    "cod",
    "trout",
    "sole",
    "pike",
    "eel"
]
VEGETABLES =[
"chick peat",
    "beet",
    "broccoli",
    "carrot",
    "cucumber",
    "eggplant",
    "egg",
    "pea",
    "potato",
    "garlic",
    "LEEK"
]
FRUIT = [
    "apple",
    "banane",
    "cherry",
    "cranberry",
    "grape",
    "plum",
    "pineapple",
    "pear"
]
CEREALS = [
    "grain"
    "rice",
    "semolina",
    "buckwheat",
    "wheat"
]
MILK_PRODUCTS = [
    "butter",
    "cheeae",
    "cream",
    "cottage cheese",
    "ice cream"
]
OTHER = [
    "coffee",
    "juice",
    "soda",
    "sugar",
    "pancake",
    "muffin",
    "marmalade",
    "vanila"
]

COLOURS = [
    "YELLOW",
    "PINK",
    "RED",
    "PURPLE",
    "ORANGE",
    "BLUE",
    "GREEN",
    "GRAY",
    "BROWN",
    "RUBY",
    "GOLDEN",
    "MINT",
    "SILVER"
]

NAME =[
    "nina",
    "sabina",
    "redjina",
    "emma",
    "kate",
    "ksenia",
    "anna",
    "anastasia",
    "maria",
    "katy",
    "sam",
    "qetuo",
    "dany",
    "oleg",
    "ruslan",
    "zahar",
    "cat",
    "anton",
    "herman",
    "alex",
    "sasha",
    "taylor",
    "ariana"
]
LAST_NAME = [
    "swift",
    "grande",
    "swan",
    "mills",
    "fuga",
    "vally",
    "karp",
    "bear",
    "panda",
    "cat",
    "ortega",
    "fallon",
    "watson",
    "redclif",
    "taylor",
    "clark",
    "stark",
    "lipa",
    "lanister",
    "dep",
    "tirell"
]

MAIL = [
    "gmail.com",
    "mail.ru",
    "campus.mephi.ru",
    "yandex.ru",
    "vk.com",
    "rambler.ru",
    "outlook.com",
    "yahoo.com",
    "mailfence.com"
]
# print(generate_category())
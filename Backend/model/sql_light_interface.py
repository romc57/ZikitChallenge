import sqlite3 as sl
from model.sql_queries import *
from pydantic import BaseModel


CATEGORIES = ['Pants', 'Shirt', 'Tank Top']


class Blogpost(BaseModel):
    name: str
    text: str
    category: str


class Product(BaseModel):
    brand: str
    name: str
    price: str
    category: str
    blogpost: int


def get_connection():
    con = sl.connect('app-db.db')
    return con


def execute_query(query):
    con = get_connection()
    try:
        with con:
            res = con.execute(query)
            return res.fetchall(), res.lastrowid
    except Exception as e:
        print('Raised exception ', e)


def stringify_conditions(condition_dict):
    output = ''
    for cond in condition_dict:
        if condition_dict[cond]:
            if output:
                output += " and {}='{}'".format(cond, condition_dict[cond])
            else:
                output += "{}='{}'".format(cond, condition_dict[cond])
    return output


def create_all_tables():
    create_blogspot_table()
    create_product_table()


def create_blogspot_table():
    execute_query(CREATE_BLOGPOST_TABLE)


def create_product_table():
    execute_query(CREATE_PRODUCT_TABLE)


def insert_new_blogspot(name, text, category):
    res, last_row_id = execute_query(INSERT_NEW_BLOGPOST.format(name, text, category))
    if res is not None:
        return last_row_id
    else:
        return False


def insert_new_product(brand, name, price, category, blogspot_id):
    res, last_row_id = execute_query(INSERT_NEW_PRODUCT.format(brand, name, price, category, blogspot_id))
    if res is not None:
        return last_row_id
    else:
        return False


def get_all_blogposts(limit=20, offset=0, name='', text='', category=''):
    query = 'SELECT id FROM blogpost'
    if name or text or category:
        query += ' WHERE '
        query += stringify_conditions({'name': name, 'text': text, 'category': category})
    query += ' limit {} offset {}'.format(limit, offset)
    blogspotgs, last_row = execute_query(query)
    if blogspotgs and blogspotgs is not None:
        output = [tup[0] for tup in blogspotgs if len(tup) > 0]
    else:
        output = list()
    return output


def get_all_products(limit=20, offset=0, brand='', name='', price='', category=''):
    query = 'SELECT id FROM product'
    if brand or name or price or category:
        query += ' WHERE '
        query += stringify_conditions({'brand': brand, 'name': name, 'price': price, 'category': category})
    query += ' limit {} offset {}'.format(limit, offset)
    products, last_row_id = execute_query(query)
    if products and products is not None:
        output = [tup[0] for tup in products if len(tup) > 0]
    else:
        output = list()
    return output


def get_blogpost_by_id(blogspot_id):
    res, last_row_id = execute_query(QUERY_BLOGPOST_ID.format(blogspot_id))
    if len(res) == 0:
        return False
    output = dict()
    output['id'] = res[0][0]
    output['name'] = res[0][1]
    output['text'] = res[0][2]
    output['category'] = res[0][3]
    res, last_row_id = execute_query(GET_ALL_PRODUCTS_BY_BLOGPOST.format(output['id']))
    output['products'] = [tup[0] for tup in res if len(tup) > 0]
    return output


def get_product_by_id(product_id):
    res, last_row_id = execute_query(QUERY_PRODUCT_ID.format(product_id))
    if len(res) == 0:
        return False
    output = dict()
    output['id'] = res[0][0]
    output['brand'] = res[0][1]
    output['name'] = res[0][2]
    output['price'] = res[0][3]
    output['category'] = res[0][4]
    output['blogpost_id'] = res[0][5]
    return output


def update_blogspot_by_id(blogspot_id, blogspot_obj: Blogpost):
    if not get_blogpost_by_id(blogspot_id):
        return False
    res, last_row_id = execute_query(UPDATE_EXISTING_BLOGPOST.format(
        blogspot_obj.name, blogspot_obj.text, blogspot_obj.category, blogspot_id
    ))
    if res is None:
        return False
    return True


def update_product_by_id(product_id: int, product: Product):
    if not get_product_by_id(product_id):
        return False
    res, last_row_id = execute_query(UPDATE_EXISTING_PRODUCT.format(
        product.brand, product.name, product.price, product.category, product.blogpost
    ))
    if res is None:
        return False
    return True


def delete_blogspot_by_id(blogspot_id):
    if not get_blogpost_by_id(blogspot_id):
        return False
    res, last_row_id = execute_query(DELETE_BLOGPOST_BY_ID.format(blogspot_id))
    if res is None:
        return False
    return get_all_blogposts()


def delete_product_by_id(product_id):
    if not get_product_by_id(product_id):
        return False
    res, last_row_id = execute_query(DELETE_PRODUCT_BY_ID.format(product_id))
    if res is None:
        return False
    return get_all_products()


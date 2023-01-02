from fastapi import FastAPI, HTTPException
from model.sql_light_interface import *
from typing import Optional


API_DEFAULT_LIMIT = 20
API_DEFAULT_OFFSET = 0


app = FastAPI()


create_all_tables()


@app.get('/blogposts')
def get_blogpost(limit: Optional[int] = API_DEFAULT_LIMIT,
                 offset: Optional[int] = API_DEFAULT_OFFSET,
                 name: Optional[str] = '',
                 category: Optional[str] = '',
                 text: Optional[str] = ''):
    res = get_all_blogposts(limit, offset, name, text, category)
    return res


@app.get('/products')
def get_products(limit: Optional[int] = API_DEFAULT_LIMIT,
                 offset: Optional[int] = API_DEFAULT_OFFSET,
                 brand: Optional[str] = '',
                 name: Optional[str] = '',
                 price: Optional[str] = '',
                 category: Optional[str] = ''):
    res = get_all_products(limit, offset, brand, name, price, category)
    return res


@app.get('/blogposts/{blogpost_id}')
def get_blogspot(blogpost_id: int):
    res = get_blogpost_by_id(blogpost_id)
    if not res:
        raise HTTPException(status_code=404, detail='blogpost was not found')
    else:
        return {'blogpost': res}


@app.get('/products/{product_id}')
def get_product(product_id: int):
    res = get_product_by_id(product_id)
    if not res:
        raise HTTPException(status_code=404, detail='product was not found')
    else:
        return {'product': res}


@app.post('/blogposts')
def add_blogspot(blogspot: Blogspot):
    if blogspot.category not in CATEGORIES:
        raise HTTPException(status_code=422, detail='Wrong category option')
    if insert_new_blogspot(blogspot.name, blogspot.text, blogspot.category):
        return {'blogpost': blogspot}
    else:
        raise HTTPException(status_code=404, detail='Error on insert')


@app.post('/products')
def add_product(product: Product):
    if product.category not in CATEGORIES:
        raise HTTPException(status_code=422, detail='Wrong category option')
    if insert_new_product(product.brand, product.name, product.price, product.category, product.blogpost):
        return {'product': product}
    else:
        raise HTTPException(status_code=404, detail='Error on insert')


@app.put('/blogposts/{blogspot_id}')
def update_blogspot(blogpost: Blogspot, blogspot_id: int):
    if blogpost.category not in CATEGORIES:
        raise HTTPException(status_code=422, detail='Wrong category option')
    if update_blogspot_by_id(blogspot_id, blogpost):
        return {'blogpost': blogpost}
    else:
        raise HTTPException(status_code=404, detail='Error on update')


@app.put('/products/{product_id}')
def update_product(product: Product, product_id: int):
    if product.category not in CATEGORIES:
        raise HTTPException(status_code=422, detail='Wrong category option')
    if update_product_by_id(product_id, product):
        return {'product': product}
    else:
        raise HTTPException(status_code=404, detail='Error on update')


@app.delete('/blogposts/{blogspot_id}')
def delete_blogspot(blogspot_id):
    res = delete_blogspot_by_id(blogspot_id)
    if res:
        return {'blogpost': res}
    else:
        raise HTTPException(status_code=404, detail='Error on delete')


@app.delete('/products/{product_id}')
def delete_product(product_id):
    res = delete_product_by_id(product_id)
    if res:
        return {'product': res}
    else:
        raise HTTPException(status_code=404, detail='Error on delete')
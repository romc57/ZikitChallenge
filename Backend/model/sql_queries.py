CREATE_BLOGPOST_TABLE = """
    CREATE TABLE IF NOT EXISTS blogpost (
        id integer PRIMARY KEY,
        name text,
        text text,
        category text
    );
"""


CREATE_PRODUCT_TABLE = """
    CREATE TABLE IF NOT EXISTS product (
        id integer PRIMARY KEY,
        brand text,
        name text,
        price text,
        category text,
        blogpost_id integer,
        FOREIGN KEY (blogpost_id) REFERENCES blogpost(id)
    );    
"""


QUERY_BLOGPOST_ID = """
    SELECT * FROM blogpost
    WHERE id={};
"""


QUERY_PRODUCT_ID = """
    SELECT * FROM product
    WHERE id={};
"""


INSERT_NEW_BLOGPOST = """
    INSERT INTO blogpost (name, text, category)
    VALUES ('{}', '{}', '{}');
"""


INSERT_NEW_PRODUCT = """
    INSERT INTO product (brand, name, price, category, blogpost_id)
    VALUES ('{}', '{}', '{}', '{}', '{}')
"""


UPDATE_EXISTING_BLOGPOST = """
    UPDATE blogpost
    SET name='{}', text='{}', category='{}'
    WHERE id={};
"""

UPDATE_EXISTING_PRODUCT = """
    UDPATE product
    SET brand='{}', name='{}', price='{}', category='{}', blogpost_id='{}'
    WHERE id={};
"""


DELETE_BLOGPOST_BY_ID = """
    DELETE FROM blogpost
    WHERE id={};
"""


DELETE_PRODUCT_BY_ID = """
    DELETE FROM product
    WHERE id={};
"""


GET_ALL_PRODUCTS_BY_BLOGPOST = """
    SELECT id 
    FROM product
    WHERE blogpost_id={}
"""


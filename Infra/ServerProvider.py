from pulumi import Output, Input, ResourceOptions
from typing import Any, Optional
from pulumi.dynamic import *
import requests
import json


class ServerArgs(object):
    server_url: Input[str]
    end_point: Input[str]
    data: Input[str]
    blogpost_id: Optional[Input[Output]]

    def __init__(self, server_url, end_point, data, blogpost_id=None):
        self.server_url = server_url
        self.end_point = end_point
        self.data = data
        self.blogpost_id = blogpost_id


class ServerProvider(ResourceProvider):

    def create(self, props):
        full_url = '{}/{}'.format(props['server_url'], props['end_point'])
        blogpost = props.get('blogpost_id', None)
        if blogpost is not None:
            data = json.loads(props['data'])
            data['blogpost'] = str(blogpost)
            data = json.dumps(data)
        else:
            data = props['data']
        response = requests.post(full_url, data=data)
        if response.status_code != 200:
            print('Error ', response.json())
        else:
            inserted_obj = response.json()
            obj_data = [inserted_obj[key] for key in inserted_obj][0]
            obj_data_str = json.dumps(obj_data)
            out = {'server_url': props['server_url'], 'end_point': props['end_point'], 'data': obj_data_str}
            insert_id = str(obj_data['id'])
            return CreateResult(id_=insert_id, outs=out)

    def delete(self, id, props):
        full_url = '{}/{}/{}'.format(props['server_url'], props['end_point'], id)
        requests.delete(full_url)


class ServerObject(Resource):
    server_url: Output[str]
    end_point: Output[str]
    data: Output[str]

    def __init__(self, name, args: ServerArgs, opts: Optional[ResourceOptions] = None):
        full_args = {'server_url': None, 'end_point': None, 'data': None, **vars(args)}
        super().__init__(ServerProvider(), name, full_args, opts)


class BlogpostObject(ServerObject):

    def __init__(self, name, server_url, post_name, post_text, post_category):
        data = json.dumps({'name': post_name, 'text': post_text, 'category': post_category})
        super().__init__(name, ServerArgs(server_url, 'blogposts', data))


class ProductObject(ServerObject):

    def __init__(self, name, server_url, brand, prod_name, price, category, blogpost: BlogpostObject):
        data = json.dumps({'brand': brand, 'name': prod_name, 'price': price, 'category': category,
                           'blogpost': 0})
        super().__init__(name, ServerArgs(server_url, 'products', data, blogpost))


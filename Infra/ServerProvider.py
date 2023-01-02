from pulumi import Output, Input, ResourceOptions
from pulumi.dynamic import *
from rest_api_calls import *


class ObjectArgs(object):
    url: Input[str]
    name: Input[str]
    text: Input[str]
    category: Input[str]

    def __init__(self, url, name, text, category):
        self.url = url
        self.name = name
        self.text = text
        self.category = category


class ObjectProvider(ResourceProvider):

    def create(self, props):
        data = {'name': props['name'], 'text': props['text'], 'category': props['category']}
        res = post_request(props['url'], data)
        outs = {"res": res, "url": props['url'], "name": props['name'], "text": props['text'], "category": props['category']}
        return CreateResult("1", outs=outs)

    def delete(self, id: str, props):
        delete_request(props)


class TableObject(Resource):
    res: Output[str]
    url: Output[str]
    name: Output[str]
    text: Output[str]
    category: Output[str]

    def __init__(self, name, args: ObjectArgs):
        super().__init__(ObjectProvider(), name, {'res': None, **vars(args)})


obj = TableObject("testst", ObjectArgs("http://127.0.0.1:8000/blogposts", "more testing", "testststst", "Pants"))

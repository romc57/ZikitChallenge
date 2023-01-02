from ServerProvider import BlogpostObject, ProductObject
from pulumi import Output
import json
import requests


SERVER_URL = r'http://127.0.0.1:8000'


build_data = [
    {
        "name": "PantsBlogPost",
        "text": "Blog post about pants",
        "category": "Pants",
        "products": [
            {
                "brand": "Nike",
                "name": "NikePants",
                "price": "400nis",
                "category": "Pants"
            },
            {
                "brand": "Adidas",
                "name": "AdidasPants",
                "price": "500nis",
                "category": "Pants"
            },
            {
                "brand": "H&M",
                "name": "HAmdMPants",
                "price": "200Dollar",
                "category": "Pants"
            }
        ]
    },

    {
        "name": "ShirtBlogPost",
        "text": "Blog post about shirt",
        "category": "Shirt",
        "products": [
            {
                "brand": "Prime",
                "name": "PrimeShirts",
                "price": "50000$",
                "category": "Shirt"
            }
        ]
    },

    {
        "name": "TankTopLife",
        "text": "Daring blog post about tank tops",
        "category": "Tank Top",
        "products": [
            {
                "brand": "Sassy",
                "name": "SassyTankTop",
                "price": "5nis",
                "category": "Tank Top"
            }
        ]
    }
]


if __name__ == '__main__':
    blogposts = list()
    products = list()
    for blogpost in build_data:
        blogposts.append(BlogpostObject(blogpost['name'], SERVER_URL, blogpost['name'], blogpost['text'],
                                        blogpost['category']))
        for product in blogpost['products']:
            products.append(ProductObject(product['name'], SERVER_URL, product['brand'], product['name'],
                                          product['price'], product['category'], blogposts[-1]))



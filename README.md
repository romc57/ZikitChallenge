# ZikitChallenge

This project has a backend rest api server and a dynamic resource provider to create resources from the server.
Make sure you have pulumi installed:

https://www.pulumi.com/docs/get-started/install/

# HowToUse

Run resource server on docker:

    $ cd ./Backend/
    $ docker build -t resource_server .
    $ docker run --rm --name resource_server -p 5000:5000 resource_server
    
    Check out the empty tables:
        http://127.0.0.1:5000/products
        http://127.0.0.1:5000/blogposts


Test pulumi dynamic resources on predefined code inside ./Infra/__main__ :

    $ cd ./Infra
    $ pip3 install -r requirements.txt
    $ pulumi login --local
    $ pulumi up
    Choose a stack or create a new one and try and creating the resources

    After resources are created checkout the tables:
        http://127.0.0.1:5000/products
        http://127.0.0.1:5000/blogposts
        http://127.0.0.1:5000/blogposts/{id}
        http://127.0.0.1:5000/products/{id}

    Remove al resources:
    
    $ pulumi down
    
    






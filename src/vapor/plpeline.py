# expose to import
__all__=[
    "say_hello"
]

def say_hello(name):
    """Print a hello message

    :param name: a name
    """
    print(f"Hello, {name}") #noqa

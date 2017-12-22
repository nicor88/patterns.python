import json


def as_json(func):
    def wrapper(*args, **kargs):
        return json.dumps(func(*args, **kargs))
    return wrapper


@as_json
def dict_name(*, name):
    return dict(name=name)


print(dict_name(name='Nicola'))

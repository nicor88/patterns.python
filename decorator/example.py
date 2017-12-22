def p_decorate(func):
    def func_wrapper(name):
        return 'added from deco {0}'.format(func(name))

    return func_wrapper


@p_decorate
def get_text(name):
    return 'your name is {0}'.format(name)


print(get_text('Nicola'))

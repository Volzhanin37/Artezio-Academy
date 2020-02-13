def get_public_attributes(x):
    return [attr for attr in dir(x) if not attr.startswith('_')]

s = 'some string'
print(get_public_attributes(s))

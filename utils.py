import bcrypt

def password_hash(password: str):

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def password_check(password: str, hashed_password: str):

    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except ValueError:
        return False


def filter_dict(dictionary: dict, keys_list=None, return_list=False):

    if not keys_list:
        keys_list = dictionary.keys()

    if return_list:
        return [value for key, value in dictionary.items() if key in keys_list]
    else:
        return {key.replace('_', ' ').capitalize(): value for key, value in dictionary.items() if key in keys_list}

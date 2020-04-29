import bcrypt

def password_hash(password: str):

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def password_check(password: str, hashed_password: str):

    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except ValueError:
        return False


def filter_dict(dictionary: dict, keys_list=None):

    if not keys_list:
        keys_list = dictionary.keys()

    new_dict = {key.replace('_', ' ').capitalize(): value for key, value in dictionary.items() if key in keys_list}
    return new_dict

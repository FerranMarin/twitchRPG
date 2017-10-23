from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "apirest": "randomkey",
}


@auth.get_password
def get_pw(username):
    """"
    Checks HTTP basic authentication through upper user dict.

    :params username: username
    :returns: boolean -- Response None or password hash.
    """
    if username in users:
        return users.get(username)
    return None

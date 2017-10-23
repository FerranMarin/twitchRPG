from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "apirest": "lk0zoibbif2gaxkyppuf1t0yaxs6x32n",
    "epi": "nxl587et0yybd81sse4m345vbteokijb"
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

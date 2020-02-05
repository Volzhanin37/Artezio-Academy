import requests


def mk_req(url):
    r = requests.get(url)
    return r

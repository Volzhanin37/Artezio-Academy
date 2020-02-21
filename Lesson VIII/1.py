import requests


def page_size(url):
    r = requests.get(url)
    return len(r.text)

print(page_size('https://google.com'))

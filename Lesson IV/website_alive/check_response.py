import make_request


def ck_res(url):
    r = make_request.mk_req(url)
    if r.status_code == 200:
        return True
    else:
        return False

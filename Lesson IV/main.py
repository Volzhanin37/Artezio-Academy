from website_alive import check_response

url = input("Введите адрес сайта: ")
if check_response.ck_res(url):
    print('сайт доступен')
else:
    print('сайт недоступен')

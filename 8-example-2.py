from urllib.parse import unquote_plus

body = b'name=krabaton&email=krabat%40test.com&text=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82+%D0%BC%D0%B8%D1%80'
parse_data = unquote_plus(body.decode(), encoding='utf-8')
result = dict([el.split('=') for el in parse_data.split('&')])
print(result)

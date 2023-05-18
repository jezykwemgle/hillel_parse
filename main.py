from urllib.parse import urlparse
def parse(query: str) -> dict:
    querys = {}
    for item in urlparse(query).query.split('&'):
        if item:
            querys[item.split('=')[0]] = item.split('=')[1]
    return querys


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    ###
    assert parse('http://example.com/name=') == {}
    assert parse('http://example.com/about.html') == {}
    assert parse('http://example.com/path/to/page?имя=дима&возраст=20') == {'имя': 'дима', 'возраст': '20'}
    assert parse('http://example.com/about.html?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/about.html?name=ferret&color=purple#') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com:443/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com:443/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/path/to/page/%D0%A2%D0%B5%D1%81%D1%82?key=%D1%8A') == {'key': '%D1%8A'}
    assert parse('http://example.com?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/about.html#?name=ferret&color=purple') == {}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}


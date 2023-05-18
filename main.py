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
    splited_cookie = {}
    for item in query.strip(';').split(';'):
        if item:
            if item.split('=', 1)[0].strip(';') and item.split('=', 1)[1].strip(';'):
                splited_cookie[item.split('=', 1)[0].strip(';').strip(' ')] = item.split('=', 1)[1].strip(';').strip(
                    ' ')
            else:
                pass
    return splited_cookie


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie(';name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima; age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User; age=28=years;') == {'name': 'Dima=User', 'age': '28=years'}
    assert parse_cookie(';name = Dima;age = 28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie(';name=Dima;;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=;age=28;;;;') == {'age': '28'}
    assert parse_cookie('id=a3fWa; Expires=Thu, 31 Oct 2021 07:28:00 GMT;') == {'id': 'a3fWa',
                                                                                'Expires': 'Thu, 31 Oct 2021 07:28:00 GMT'}
    assert parse_cookie('__utma=13103r6942.2918') == {'__utma': '13103r6942.2918'}
    assert parse_cookie('name=bijaya; comment=Comment1; expires=Mon;  path=/; domain=.google.com;  SameSite=none; '
                        'Max-Age=244114; Version=1.2; priority=high;') == {'name': 'bijaya', 'comment': 'Comment1',
                                                                           'expires': 'Mon', 'path': '/',
                                                                           'domain': '.google.com', 'SameSite': 'none',
                                                                           'Max-Age': '244114',
                                                                           'Version': '1.2', 'priority': 'high'}


def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


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


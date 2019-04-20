import json
from urllib import request


# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=

def getCountries(s, p):
    response = request.urlopen(f'https://jsonmock.hackerrank.com/api/countries/search/?name={s}')
    data = json.loads(response.read())

    total_pages = data.get('total_pages')
    total_count = 0
    names = set()

    for page in range(1, total_pages + 1):
        for country in data.get('data'):
            if int(country['population']) > p and country['name'] not in names:
                total_count += 1

        response = request.urlopen(f'https://jsonmock.hackerrank.com/api/countries/search/?name={s}?page={page}')
        data = json.loads(response.read())

    return total_count


if __name__ == '__main__':
    print(getCountries('un', 100090))

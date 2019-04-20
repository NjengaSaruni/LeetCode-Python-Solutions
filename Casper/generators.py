import json

class SearchByTag:
    def __init__(self, data_file, query_tag):
        with open(data_file) as data:
            movies = json.load(data)
            self.items = tuple(movies['items'])
            self.query = query_tag

    def search(self):
        for item in self.items:
            if 'tags' in item and self.query in item['tags']:
                yield item

    def first(self):
        return next(self.search())

if __name__ == '__main__':
    search = SearchByTag('./movies.json', 'crime')
    print(search.first())
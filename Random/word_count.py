import unittest
def most_frequent(s):
    words = s.split(' ')
    _map = dict()
    for word in words:
        if _map.__contains__(word):
            _map[word] += 1
        else:
            _map[word] = 1

    print(_map)
    most = 0
    ans = ''

    for key in _map.keys():
        if _map[key] > most:
            ans = key
            most = _map[key]

    return ans

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.function = most_frequent

    def test_simple(self):
        string = 'There was once a bad person that had a big bad apple and a cow.'
        self.assertEqual(self.function(string), 'a')

def say_hello(name):
    # you can print to STDOUT to debug if you need to:
    print(name)

    # but to complete the challenge you need to return a value
    if name:
        answer = 'Hello, %s!' % name
    else:
        answer = 'Hello there!'
    return answer


import unittest

# These example test cases are editable, feel free to add
# your own tests to debug your code.

# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_should_say_hello(self):
    self.assertEqual(say_hello("Qualified"), "Hello, Qualified!")
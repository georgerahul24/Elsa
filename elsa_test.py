import unittest

from Magic import indexer,theme,usernames

def sum(a,b):
    return a+b

class SimpleTest(unittest.TestCase):
    #def test<anyname>(self): should be the format for making a function to test
    def testadd(self):
        self.assertEqual(sum(1,2),3)
    def testindexfiles(self):
        self.assertEqual(indexer.index_files(), None)
    def testtheme(self):
        self.assertIsNotNone(theme.read_theme())
    def testusernames(self):
        self.assertEqual(usernames.verify_usernames(),False)


if __name__ == '__main__':
    unittest.main()
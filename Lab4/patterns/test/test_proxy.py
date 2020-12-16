import unittest
from patterns.proxy import RealSubject, Proxy

class proxyTest(unittest.TestCase):

    def setUp(self) -> None:
        self._real = RealSubject()
        self._connection = Proxy(self._real)

    def test_haveacces(self):
        listofusers = ['alexeyzer', "andrey-kireev", "valerdon"]
        for i in listofusers:
            with self.subTest(i=i):
                self.assertTrue(self._connection.check_access(i))
    def test_noacces(self):
        listofusers = ['vaksina', "gavrilov", "perlin"]
        for i in listofusers:
            with self.subTest(i=i):
                self.assertFalse(self._connection.check_access(i))

    def test_request(self):
        self.assertEqual(self._connection.request('alexeyzer', "select * from todo"), "some data")
        self.assertEqual(self._connection.request('valerdon', "select * from did"), "some data")


if __name__ == '__main__':
    unittest.main()
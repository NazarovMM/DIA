import unittest
from patterns.strategy import Navigator, Strategypublictransport, StrategybyFoot

class proxyTest(unittest.TestCase):

    def setUp(self) -> None:
        self._context = Navigator(Strategypublictransport())

    def test_bypublictransportsucces(self):
        self.assertEqual(self._context.do_some_business_logic('A', 'B'), ['busA'])

    def test_bypublictransportdeny(self):
        self.assertEqual(self._context.do_some_business_logic('A', 'g'), None)

    def test_byfootrue(self):
        self._context.strategy = StrategybyFoot()
        self.assertEqual(self._context.do_some_business_logic('A', 'B'), "you can go by foot from place A to B by foot")
    def test_byfootnoplace(self):
        self._context.strategy = StrategybyFoot()
        self.assertEqual(self._context.do_some_business_logic('A', 'R'), None)

    def test_byfootnoway(self):
        self._context.strategy = StrategybyFoot()
        self.assertEqual(self._context.do_some_business_logic('A', 'F'), "no way by Foot")

if __name__ == '__main__':
    unittest.main()
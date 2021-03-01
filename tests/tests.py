import unittest
from netaddr import IPSet, IPAddress


with open("iplist.txt", "r") as checkfile:
    cidr = checkfile.readlines()

class Tests(unittest.TestCase):

    def test_true(self):
        self.assertTrue(IPAddress("64.190.60.1") in IPSet(cidr))
        self.assertTrue(IPAddress("2.56.32.1") in IPSet(cidr))

    def test_false(self):
        self.assertFalse(IPAddress("192.168.1.1") in IPSet(cidr))
        self.assertFalse(IPAddress("192.168.10.1") in IPSet(cidr))

    def test_existence(self):
        self.assertIsNotNone(cidr)

    def test_notempty(self):
        self.assertTrue(len(cidr))

if __name__ == "__main__":
    unittest.main()
    
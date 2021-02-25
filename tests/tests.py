from netaddr import IPNetwork, IPAddress
import unittest

class Tests(unittest.TestCase):

    def test_true(self):
        self.assertTrue(IPAddress("64.190.60.1") in IPNetwork("64.190.60.0/23"))

    def test_false(self):
        self.assertFalse(IPAddress("192.168.10.1") in IPNetwork("64.190.60.0/23"))

if __name__ == "__main__":
    unittest.main()
    
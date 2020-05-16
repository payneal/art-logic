import unittest
from encoding import Encoding

class Test_Encoding(unittest.TestCase):

    def setUp(self):
        self.encoder = Encoding();

    def tearDown(self):
        self.encoder = None
    
    def test_single_character(self):
        decimal = self.encoder.encode_decimal("A")
        self.assertEqual(decimal, 16777217)
        hex_value = self.encoder.encode_hex("A")
        self.assertEqual( int(hex_value,16), int('0x01000001',16))


    def test_full_bundle(self):
        decimal = self.encoder.encode_decimal("FRED")
        self.assertEqual(decimal, 251792692)
        hex_value = self.encoder.encode_hex("FRED")
        self.assertEqual( int(hex_value,16), int('0x0F020d34',16))

    def test_non_alphanumerics(self):
        decimal = self.encoder.encode_decimal(" :^)")
        self.assertEqual(decimal, 79094888)
        hex_value = self.encoder.encode_hex(" :^)")
        self.assertEqual( int(hex_value,16), int('0x04B6E468',16))
    
    def test_foo_with_space(self):
        decimal = self.encoder.encode_decimal(" foo")
        self.assertEqual(decimal, 250662636)

    def test_foot(self):
        decimal = self.encoder.encode_decimal("foot")
        self.assertEqual(decimal, 267939702)

    def test_BIRD(self):
        decimal = self.encoder.encode_decimal("BIRD")
        self.assertEqual(decimal, 251930706)

    def test_periods(self):
        decimal = self.encoder.encode_decimal("....")
        self.assertEqual(decimal, 15794160)

    def test_carrots(self):
        decimal = self.encoder.encode_decimal("^^^^")
        self.assertEqual(decimal, 252706800)

    def test_Whoot(self):
        decimal = self.encoder.encode_decimal("Woot")
        self.assertEqual(decimal, 266956663)

    def test_no(self):
        decimal = self.encoder.encode_decimal("no")
        self.assertEqual(decimal, 53490482)
    
    def test_email(self):
        decimal = self.encoder.encode_decimal("a@b.")
        self.assertEqual(decimal, 131107009)

    def test_my_email(self):
        decimal = self.encoder.encode_decimal("me@a")
        self.assertEqual(decimal, 263197451)




if __name__ == "__main__":
    unittest.main()

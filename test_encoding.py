import unittest
from encoding import Encoding

class Test_Encoding(unittest.TestCase):

    def setUp(self):
        self.encoder = Encoding()

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

    def test_foo(self):
        decimal = self.encoder.encode_decimal("foo")
        self.assertEqual(decimal, 124807030)

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

    # ----------- Part 2 ----------------------------
    
    def test_endcode_array_tacocat(self):
        encoded = self.encoder.encode("tacocat")
        self.assertEqual(encoded, [267487694, 125043731])
    
    def test_decode_FRED(self):
        decoded = self.encoder.decode_decimal(251792692)
        self.assertEqual(decoded, "FRED")
    
    def test_decode_array_tacocat(self):
        decoded = self.encoder.decode( [267487694, 125043731])
        self.assertEqual(decoded, "tacocat") 

    def test_decode_array_never_odd(self):
        decoded = self.encoder.decode([
            267657050, 233917524, 234374596, 
            250875466, 17830160])
        self.assertEqual(decoded, "never odd or even") 

    def test_decode_array_larger(self):
        decoded = self.encoder.decode([
            267394382, 167322264, 66212897, 
            200937635, 267422503])
        self.assertEqual(decoded, "lager, sir, is regal") 

    def test_decode_array_go_hang(self):
        decoded = self.encoder.decode([
            200319795, 133178981, 234094669, 
            267441422, 78666124, 99619077, 
            267653454, 133178165, 124794470])
        self.assertEqual(
                decoded, "go hang a salami, I'm a lasagna hog") 

    def test_decode_array_engad(self):
        decoded = self.encoder.decode([
            267389735, 82841860, 267651166, 
            250793668, 233835785, 267665210, 
            99680277, 133170194, 124782119])
        self.assertEqual(
                decoded, "egad, a base tone denotes a bad age") 
 
    def test_bothways(self):
        self.assertEqual(
                "bothways", self.encoder.decode(
                    self.encoder.encode("bothways")))

if __name__ == "__main__":
    unittest.main()

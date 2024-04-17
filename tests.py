import unittest
from function import fn

conversions = """
1 kg = 1000 g
1 mile = 1.609 km
1 km = 1000 m
1 m = 100 cm
1 cm = 10 mm
1 pound = 0.454 kg
"""

single_line_string_conversions = "1 kg = 1000 g 1 mile = 1.609 km 1 km = 1000 m 1 m = 100 cm 1 cm = 10 mm 1 pound = 0.454 kg"

malformed_conversions = """
1 kg == 1000 g
1 mile = 1.609 km
1 km = 1000 m
1 m = 100 cm
1 cm = 10 mm
1 pound = 0.454 kg
"""


class Test(unittest.TestCase):

    # Functional tests
    def test_kg_g(self):
        result = fn(conversions, "kg", 1, "g")
        expected_value = 1 * 1000
        self.assertEqual(result, expected_value)

    def test_km_m(self):
        result = fn(conversions, "km", 1, "m")
        expected_value = 1 * 1000
        self.assertEqual(result, expected_value)

    def test_m_cm(self):
        result = fn(conversions, "m", 1, "cm")
        expected_value = 1 * 100
        self.assertEqual(result, expected_value)

    def test_cm_mm(self):
        result = fn(conversions, "cm", 1, "mm")
        expected_value = 1 * 10
        self.assertEqual(result, expected_value)
    
    def test_mile_km(self):
        result = fn(conversions, "mile", 1, "km")
        expected_value = 1 * 1.609
        self.assertEqual(result, expected_value)
    
    # Multi level/ non direct conversion tests 
    def test_g_pound(self):
        result = fn(conversions, "g", 1, "pound")
        expected_value = 1 * 0.001 * 2.202643171806167
        self.assertAlmostEqual(result, expected_value, places=3)

    def test_mm_mile(self):
        result = fn(conversions, "mm", 1, "mile")
        expected_value = 1 * 0.1 * 0.01 * 0.001 * 0.6215040397762586
        self.assertAlmostEqual(result, expected_value, places=3)

    # Edge cases
    def test_single_line_string(self):
        result = fn(single_line_string_conversions, "kg", 1, "g")
        expected = None
        self.assertEqual(result, expected)

    def test_malformed_conversion_string(self):
        result = fn(malformed_conversions, "kg", 1, "g")
        expected = None
        self.assertEqual(result, expected)

    def test_amount_input_0(self):
        result = fn(conversions, "cm", 0, "m")
        expected = 0 * 10.0
        self.assertEqual(result, expected)

    def test_really_big_number_km_mm(self):
        result = fn(conversions, "km", 100000, "m")
        expected = 100000 * 1000.0
        self.assertAlmostEqual(result, expected, places=1)


if __name__ == '__main__':
    unittest.main()
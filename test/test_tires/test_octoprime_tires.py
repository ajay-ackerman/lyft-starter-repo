import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):

    def test_should_be_serviced(self):
        tires = OctoprimeTires([0.8, 0.95, 0.7, 0.8])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = OctoprimeTires([1.0, 1.0, 1.0, 0.0])
        self.assertFalse(tires.needs_service())
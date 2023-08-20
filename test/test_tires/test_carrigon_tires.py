import unittest
from tires.carrigan_tires import CarrigonTires

class TestCarrigonTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = CarrigonTires([0.8, 0.95, 0.7, 0.8])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = CarrigonTires([0.7, 0.8, 0.6, 0.8])
        self.assertFalse(tires.needs_service())
import unittest
import sys
sys.path.append("../")
from OrderCabins_Class import *

class TestOrderCabins_Class(unittest.TestCase):
	def setUp(self):
		self.oc = OrderCabins()

	def tearDown(self):
		pass

	def test_ValidateCabinNo(self):
		self.assertFalse(self.oc.ValidateCabinNo("x"))
		self.assertTrue(self.oc.ValidateCabinNo("1"))
		self.assertFalse(self.oc.ValidateCabinNo("0"))
		self.assertFalse(self.oc.ValidateCabinNo("11"))
	

if __name__ == "__main__":
	unittest.main()
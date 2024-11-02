import typing
import unittest
from unittest.mock import Mock

def add_numbers_with_optional(a: int, b: typing.Optional[int] = None) -> int:
	if b is None:
		return a
	return a + b

class TestAddNumbers(unittest.TestCase):

	def test_add_numbers_with_optional_type_check(self):
		result = add_numbers_with_optional(10)
		self.assertIsInstance(result, int)

	def test_add_numbers_with_optional_value(self):
		result = add_numbers_with_optional(10, 20)
		self.assertEqual(result, 30)

	def test_add_numbers_with_mocking(self):
		mock_b = Mock(return_value=15)
		result = add_numbers_with_optional(10, mock_b())
		self.assertEqual(result, 25)

if __name__ == "__main__":
	unittest.main()

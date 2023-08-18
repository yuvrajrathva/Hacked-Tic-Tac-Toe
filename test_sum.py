import unittest

class TestSum(unittest.TestCase):
  def test_sum(self):
    data = [1,2]
    result = sum(data)
    self.assertEqual(result, 3, "Answer should be 3.")

  def test_sum_tuple(self):
    data = [1,1]
    result = sum(data)
    self.assertEqual(result, 2, "Answer should be 3.")
from statistics import median
import unittest
#from ..main.service.math_service import calculate_min,calculate_max
import main.service.math_service as service

class MathServiceTestCase(unittest.TestCase):
    def test_min_returning_correct_mins(self):
        list_of_numbers=[1,2,3,4]
        quantifier=2
        mins = service.calculate_min(list_of_numbers,quantifier)
        expected_result=[1,2]
        self.assertListEqual(expected_result,mins)

    def test_min_return_no_mins_when_quantifier_zero(self):
        list_of_numbers=[1,2,3,4]
        quantifier=0
        mins = service.calculate_min(list_of_numbers,quantifier)
        self.assertEqual(len(mins),0)

    def test_max_returning_correct_maxs(self):
        list_of_numbers=[1,2,3,4]
        quantifier=2
        maxs = service.calculate_max(list_of_numbers,quantifier)
        expected_result=[4,3]
        self.assertListEqual(expected_result,maxs)

    def test_max_return_no_maxs_when_quantifier_zero(self):
        list_of_numbers=[1,2,3,4]
        quantifier=0
        maxs = service.calculate_max(list_of_numbers,quantifier)
        self.assertEqual(len(maxs),0)

    def test_average_returning_correct_average(self):
        list_of_numbers=[1,2,3,4]
        average = service.calculate_average(list_of_numbers)
        expected_result=2.5
        self.assertEqual(expected_result,average)

    def test_average_raise_error_when_list_is_empty(self):
        list_of_numbers=[]
        with self.assertRaises(ValueError):
          average = service.calculate_average(list_of_numbers)

    def test_median_returning_correct_median(self):
        list_of_numbers=[1,2,3,4]
        median = service.calculate_median(list_of_numbers)
        expected_result=2.5
        self.assertEqual(expected_result,median)

    def test_median_raise_error_when_list_is_empty(self):
        list_of_numbers=[]
        with self.assertRaises(ValueError):
          median = service.calculate_median(list_of_numbers)

    def test_percentile_returning_correct_percentile(self):
        list_of_numbers=[1,2,3,4,5]
        quantifier=50
        percentile = service.calculate_percentile(list_of_numbers,quantifier)
        expected_result=3
        self.assertEqual(expected_result,percentile)

    def test_percentile_raise_error_when_list_is_empty(self):
        list_of_numbers=[]
        quantifier=50
        with self.assertRaises(ValueError):
          median = service.calculate_percentile(list_of_numbers,quantifier)